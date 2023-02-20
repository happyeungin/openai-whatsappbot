from django.conf import settings
from django.contrib.auth.models import User
from .models import *
from .ai import *
import requests


def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = { "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": phoneNumber,
                "type": "text",
                "text": {"body": message}
                }

    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()
    return ans

# phoneNumber = "85269709752"
# message = "Hello There!!!!!!"

# sendWhatsAppMessage(phoneNumber, message)
def handleWhatsAppChat(fromId, profileName, phoneId, text):
    try:
        chat = InstructionContext.objects.get(profile__phoneNumber=fromId)
    except:
        if User.objects.filter(username=phoneId).exists():
            user = User.objects.get(username=phoneId)
            user_profile = user.profile

        else:        
        ##Creating a user
            user = User.objects.create_user(
            username=phoneId,
            email="123123@gmail.com",
            password="wowowow",
            first_name=profileName,
            )

        #Create a profile
            user_profile = Profile.objects.create(
            user=user,
            phoneNumber=fromId,
            phoneId=phoneId
            )

        #Create a chat session
        chat = InstructionContext.objects.create(
        profile=user_profile
        )

        message = "隨便問我野啦!😃 Ask me anything!"
        sendWhatsAppMessage(fromId, message)

    # chat.instruction = chat.instruction + text
    if len(chat.instruction) >= 300:
         chat.instruction = text
         chat.save()
         message = "內容太多記唔哂, 而家由頭傾過喇!🤣 Too much info for me, Let's restart our chat!"
         sendWhatsAppMessage(fromId, message)
         message = startPrompt(chat.instruction)
         sendWhatsAppMessage(fromId, message)
    else:
        chat.instruction = chat.instruction + text
        chat.save()
        message = startPrompt(chat.instruction)
        sendWhatsAppMessage(fromId, message)



