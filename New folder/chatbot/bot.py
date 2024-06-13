def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if 'hello' in user_input:
            print("Chatbot: Hello! How are you?")
        
        elif 'can you help me' in user_input:
            print("Chatbot: yes how can i assist you today?")
        
        elif 'who created you' in user_input or 'good' in user_input:
            print("Chatbot: gungun")
        
        elif 'help' in user_input:
            print("Chatbot: Sure, I'm here to help! What do you need assistance with?")
        
        elif 'what is codsoft' in user_input:
            print("Chatbot:CodSoft are IT services and IT consultancy that specializes in creating innovative solutions for businesses. We are passionate about technology and believe in the power of software to transform the world.")
        
        elif 'bye' in user_input or 'exit' in user_input or 'quit' in user_input:
            print("Chatbot: Goodbye! Have a nice day!")

        # elif 'What is your name' in user_input:
        #     print("you can call me ai chat_bot")
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please retype ?")

chatbot()