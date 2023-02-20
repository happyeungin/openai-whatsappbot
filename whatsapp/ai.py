import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def startPrompt(instruction):

    response = openai.Completion.create(
        model="text-curie-001",
        # prompt="Reply(maximum 300 characters) in the language of the context.# Context:{} #".format(instruction),
        prompt=instruction,
        # prompt=instruction,
        temperature=0.7,
        max_tokens=600,
        n=1
    )

    if 'choices' in response:
        if len(response['choices'])>=0:
            answer = response['choices'][0]['text']
            # answer.replace('\n', '<br/>')
            return answer
        else:
            return ''
    
    else:
        return ''