from django.shortcuts import render
from django.contrib.auth.models import User
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
        print(data)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                for entry in data['entry']:

                    if entry['changes'][0]['value']['contacts']:
                    # phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        text = entry['changes'][0]['value']['messages'][0]['text']['body']
                        profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        handleWhatsAppChat(fromId, profileName, text)
                        # whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                    else:
                        pass
                    # message = 'RE:{} was received'.format(text)
                    # sendWhatsAppMessage(fromId, message)

            else:
                pass

        else:
            pass

        return HttpResponse('success', status=200)
