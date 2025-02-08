import os
import google.generativeai as genai


genai.configure(api_key="Your Api Key")


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Start chat session
chat_session = model.start_chat(history=[])

print("Chatbot: Hello! How can I assist you today? (Type 'exit' to quit)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = chat_session.send_message(user_input)
    print("Chatbot:", response.text)
