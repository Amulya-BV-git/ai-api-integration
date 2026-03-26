import requests
import os
API_URL="https://api-interface.huggingface.co/models/huggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": f"Bearer{os.getenv('HUGGINGFACE_API_KEY')}"}
def query_huggingface(prompt):
    response = requests.post (API_URL,headers=headers, json={"inputs": prompt})
    try:
        return  response .json()[0] ["generated_text"]
    except Exception as e:
        return f"Error: {response .text}"

user_input = input("Enter ypur prompt:")
print(query_huggingface(user_input))
