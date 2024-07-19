from fastapi import FastAPI, Request, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
import uvicorn
from pkg.classes import DialogflowWebhookRequest
from pkg.functions import dialogflowFunctions
from pkg.time import timing_middleware

app = FastAPI(version="0.1.0")


## Inicio de vistas para el UserInterfase (Webhook)
static_directory = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_directory), name="static")

@app.get("/", include_in_schema=False)
async def mainPage():
    html_file = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    return FileResponse(html_file)
    
## Final de vistas para el UserInterface (Webhook)

app.middleware("http")(timing_middleware)

## Solicitud POST para recibir llamadas de Dialogflow a nuestro Webhook
@app.post("/dialogflow-webhook-connection", description="Webhook calls made by Dialogflow")
async def webhook(request: Request):
    request_data = await request.json()
    webhook_request = DialogflowWebhookRequest(**request_data)
    intent_name = webhook_request.queryResult['intent']['displayName']
    
    response_data = dialogflowFunctions(intent_name)
    
    return JSONResponse(response_data)

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
