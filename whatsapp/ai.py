import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def startPrompt(instruction):

    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt="{}".format(instruction),
        prompt=instruction,
        temperature=0.7,
        max_tokens=300,
        n=1
    )

    if 'choices' in response:
        if len(response['choices'])>=0:
            answer = response['choices'][0]['text']
            return answer
        else:
            return ''
    
    else:
        return ''