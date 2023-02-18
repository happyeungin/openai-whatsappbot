from django.conf import settings
import requests

def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authoriztion": settings.WHATSAPP_TOKEN}
    payload = { "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": phoneNumber,
                "type": "text",
                "text": {"body": message}
                }

    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()

phoneNumber = "85269709752"
message = "Hello There!!!!!!"

sendWhatsAppMessage(phoneNumber, message)
