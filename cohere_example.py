import os
import cohere 

api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)
def chat():
    try:
        user_input = input("Enter your prompt:")

        response = co.chat(
            message=user_input)
        print("\nResponse:")
        print(response.text)
    except Exception as e:
        print("Error:", e)
chat()