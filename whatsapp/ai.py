import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def startPrompt(instruction):

    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     # prompt="Reply in the context language(maximum 200 characters)# Context:{} #".format(instruction),
    #     prompt=instruction + "\n",
    #     temperature=0.7,
    #     max_tokens=512,
    #     n=1
    # )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", "content": instruction + "\n",
            }
        ],
        temperature=0.7,
        max_tokens=512,
        n=1
    )


    if 'choices' in response:
        if len(response['choices'])>=0:
            answer = response['choices'][0]['message']['content']
            # answer.replace('\n', '<br/>')
            return answer
        else:
            return ''
    
    else:
        return ''