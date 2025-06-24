# 🤖 UniBot by UniVerse (Offline Mode v1)
# Author: Kam & GPT | Purpose: Offline truth assistant

import datetime
import os

def log_conversation(user_input, bot_response):
    with open("logs/unibot_log.txt", "a") as f:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time_now}] You: {user_input}\n")
        f.write(f"[{time_now}] UniBot: {bot_response}\n\n")

def answer(question):
    q = question.lower()
    
    # Basic local knowledge base
    if "your name" in q:
        return "I'm UniBot, your truth assistant."
    elif "creator" in q or "who made you" in q:
        return "I was created by Kam as part of the UniVerse OS."
    elif "xp" in q:
        return "You can check your XP using the CLI or GUI wallet."
    elif "will" in q:
        return "You can write your Will using the 'will' command or GUI button."
    elif "help" in q:
        return "Ask me anything about your OS, Will, XP, logs, or tools."
    elif "unistore" in q:
        return "UniStore is your local app market. Use it in the CLI to install tools."
    elif "quit" in q:
        return "Goodbye for now."
    else:
        return "Hmm... I don't know that yet. Try asking about: Will, XP, UniStore, Purpose."

def run_unibot():
    print("🤖 UniBot by UniVerse (Offline Mode)")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("UniBot: Goodbye, Kam.")
            break

        response = answer(user_input)
        print("UniBot:", response)
        log_conversation(user_input, response)

if __name__ == "__main__":
    run_unibot()
