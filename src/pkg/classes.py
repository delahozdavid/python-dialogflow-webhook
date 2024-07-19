from pydantic import BaseModel

## clase utilizada para formato de diccionario a los llamados del Webhook
class DialogflowWebhookRequest(BaseModel):
    queryResult: dict
    
    