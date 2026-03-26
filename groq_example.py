# 1. API COMFIGURATION
from groq import Groq
import os 

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

#2. QUERY FUNCTION
def query_ai(promt):
    try:
        response = client.chat.completions.create (
            model= "llama-3.1-8b-instant",
            messages = [{"role":"user","content":promt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
#3. MAIN EXECUTION
if __name__ == "__main__":
    prompt = input("Enter your prompt:")
    result = query_ai(prompt)
    print("\nAI Response:\n" )
    print(result)
