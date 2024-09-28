from mistralai import Mistral
from config import AI_TOKEN

async def generate(content):
    s = Mistral(
        api_key=AI_TOKEN,
    )
    
    # Получение ответа от модели Mistral
    res = await s.chat.complete_async(model="mistral-small-latest", messages=[
        {
            "content": content,
            "role": "user",
        },
    ])
    
    # Проверка, содержит ли ответ список 'choices'
    if res and hasattr(res, 'choices') and res.choices:
        return res.choices[0].message.content  # Доступ к контенту первого выбора

    return "No response from AI"
