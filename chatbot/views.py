from django.shortcuts import render

# Create your views here.
import json
import requests, random, re
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .bot_logic import LOGIC_RESPONSES


# this is the token verifer
VERIFY_TOKEN = "f42cb9333ba30e22e350b98d285ab5ce6316bf74f557e55100"

"""

FB_ENDPOINT & PAGE_ACCESS_TOKEN
Come from the next step.

"""

FB_ENDPOINT = 'https://graph.facebook.com/v4.0/'

PAGE_ACCESS_TOKEN = "EAAqYtw8BzVoBAPhDgutNNtP0vEqi92fehfAULSs40jZCqsgIxqkESXgI0ctxDukQdPBY5LpGEVxaNriVv3nlLWrYpVsa41djJCG50xmTgjxGFXZCkr4gR7nKvISmAqZBtU22I4MFQL4nEb2c3DosmZAZAPn9QeBRwJG0bPr6TOsVi1EEUw1W7"  



def parse_and_send_fb_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    msg = None
    for token in tokens:
        if token in LOGIC_RESPONSES:
            msg = random.choice(LOGIC_RESPONSES[token])
            break
        
    if msg is not None:                 
        endpoint = "{FB_ENDPOINT}/me/messages?access_token={PAGE_ACCESS_TOKEN}"
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":msg}})
        status = requests.post(
            endpoint, 
            headers={"Content-Type": "application/json"},
            data=response_msg)
        print(status.json())
        return status.json()
    return None
        
        
class FacebookWebhookView(View):
    @method_decorator(csrf_exempt) # required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) #python3.6+ syntax
    
    '''
    hub.mode
    hub.verify_token
    hub.challenge
    Are all from facebook. We'll discuss soon.
    '''
    def get(self, request, *args, **kwargs):
        hub_mode   = request.GET.get('hub.mode')
        hub_token = request.GET.get('hub.verify_token')
        hub_challenge = request.GET.get('hub.challenge')
        if hub_token != VERIFY_TOKEN:
            return HttpResponse('Error, invalid token', status=403)
        return HttpResponse(hub_challenge)
            

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    fb_user_id = message['sender']['id'] # sweet!
                    fb_user_txt = message['message'].get('text')
                    if fb_user_txt:
                        parse_and_send_fb_message(fb_user_id, fb_user_txt)
        return HttpResponse("Success", status=200)
