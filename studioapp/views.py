from django.shortcuts import render
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


def generate(request):
        if request.method == "POST":
            input=request.POST.get('input')
            result=scriptgenerate(input)
            return render(request,'script_studio/index.html',{'result':result})
        else:
            return render(request,'script_studio/index.html')

def scriptgenerate(input):
    client = OpenAI(
        api_key=os.getenv('api_key')
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input,
            }
        ],
        model="gpt-3.5-turbo",
    )
    Result=chat_completion.choices[0].message.content
    return Result
    




# client = OpenAI(
# api_key="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",
# )

# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": input}],
#     stream=True,
# )
# for part in stream:
#     print(part.choices[0].delta.content or "")