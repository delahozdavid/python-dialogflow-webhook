import time
from fastapi import Request, Response
from pkg.database import create_pool, webhook_logs

async def timing_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    pool = await create_pool()
    if pool is None:
        print("No se pudo crear el pool de conexiones a la base de datos")
        return response

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(start_time))
    elapsed_time = round(process_time, 2)

    await webhook_logs(pool, request.headers.get("webhookcall-id"), request.url.path, response.status_code, timestamp, elapsed_time)

    return response
