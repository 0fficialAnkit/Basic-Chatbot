import random
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey",["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"how are you ?",["I'm doing well, thank you!", "I'm fine, thanks for asking.", "I'm great! How about you?"]],
    [r"what's your name ?",["You can call me Jarvis.", "I'm Chatbot, nice to meet you!"]],
    [r"what can you do ?",["I can help you with various tasks like answering questions, providing information, or just having a chat."]],
    [r"who created you ?",["I was created by Ankit.", "My creators are the wonderful developers at Ikigai."]],
    [r"where are you from ?",["I exist in the digital realm, so you could say I'm from the internet!"]],
    [r"tell me a joke|jokes",["How does the ocean do not say hi? It waves!", "I told my wife she was drawing her eyebrows too high. She looked surprised!"]],
    [r"(.*) (joke|jokes)",["Why did the scarecrow win an award? Because he was outstanding in his field!"]],
    [r"quit",["Bye! Take care.", "Goodbye!", "Come back soon!"]],
    [r"(.*)",["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure I follow."]]]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm a chatbot. You can ask me anything or just say hi. If you want to end the conversation, type 'quit'.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    chat()
