from openai import OpenAI
from config import API_KEY

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com",
)

resp=client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you help me with a coding problem?"}
    ],
    temperature=0.7,
)# 随机性旋钮：0=几乎每次输出一样（稳），越大越天马行空（浪）

print(resp.choices[0].message.content)