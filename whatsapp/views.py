from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .functions import *
import json


# Create your views here.
def home(request):
    return render(request, 'whatsapp/index.html', {})



@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = '2dc84afb-4bc9-46e3-a750-049bf6cf0483'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)


    if request.method == 'POST':
        data = json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        phoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                        profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        messageId = entry['changes'][0]['value']['messages'][0]['id']
                        timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
                        text = entry['changes'][0]['value']['messages'][0]['text']['body']

                        phoneNumber = "85269709752"
                        message = 'RE:{} was received'.format(text)
                        sendWhatsAppMessage(phoneNumber, message)

                except:
                    pass

        return HttpResponse('success', status=200)
