import asyncpg
import uuid
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Configuración del acceso a la base de datos
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

async def create_pool():
    try:
        pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        return pool
    except Exception as e:
        print(f"Error al crear el pool de conexiones: {e}")

async def webhook_logs(pool, webhookcall_id, details, result_code, timestamp, time_elapsed):
    async with pool.acquire() as connection:
        try:
            # Si el `webhookcall_id` no se pasa, generarlo
            if not webhookcall_id:
                webhookcall_id = str(uuid.uuid4())
            
            # Convertir timestamp a datetime.datetime si es una cadena
            if isinstance(timestamp, str):
                timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            
            # Convertir time_elapsed a una cadena si es un float
            if isinstance(time_elapsed, float):
                time_elapsed = timedelta(microseconds=time_elapsed)
            
            # Realizar la inserción en la base de datos
            await connection.execute("""
                INSERT INTO webhook_logs (webhookcall_id, details, result_code, timestamp, time_elapsed)
                VALUES ($1, $2, $3, $4, $5)
            """, webhookcall_id, details, result_code, timestamp, time_elapsed)
            print(f"Registro ID: {webhookcall_id} agregado")
        except Exception as e:
            print(f"Error al registrar en la base de datos: {e}")
