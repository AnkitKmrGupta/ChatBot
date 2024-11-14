import openai

# Directly set your API key
openai.api_key = "sk-proj-apu2A70sFzYfIjQwgR0yB7eKFxQdQWXB48c05_ntXmIVGIvNvAojpz7Q3xuaRxNEbUa2D7OmE3T3BlbkFJRAgycoxkAM2VnEL9NmXN31tk7wzJkbFNI1I8iFv87VBJLMi-5f6CMQT8n-0awBCfETEf0V80"

def chatbot():
    print("ChatGPT: Hello! Ask me anything. Type 'exit' to quit.\n")
    
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("ChatGPT: Goodbye!")
            break

        # Add user message to the conversation history
        conversation_history.append({"role": "user", "content": user_input})
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history
            )
            
            # Extract and print the assistant's reply
            assistant_message = response['choices'][0]['message']['content']
            print(f"ChatGPT: {assistant_message}\n")
            
            # Add the assistant's reply to the conversation history
            conversation_history.append({"role": "assistant", "content": assistant_message})
        
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")
            break

# Run the chatbot
chatbot()
