import random
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Responses dictionary with more intents
responses = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hi there! How's it going?",
        "Hey! What can I do for you today?",
        "Greetings! How can I help you today?"
    ],
    "goodbye": [
        "Goodbye! It was nice talking to you. Have a great day!",
        "See you later! Take care!",
        "Bye! Feel free to reach out anytime!",
        "Goodbye! Wishing you all the best!"
    ],
    "help": [
        "I can assist you with a variety of things, like setting reminders, providing weather updates, answering general questions, and more. How can I help?",
        "Need help? I can guide you with any issues you're facing, from tech support to simple questions.",
        "I'm here to help! What would you like assistance with today?",
        "Do you need help with something specific? I can help with tasks like making reservations, answering questions, and more."
    ],
    "gratitude": [
        "You're welcome! Happy to help!",
        "No problem! I'm here anytime you need assistance.",
        "You're welcome! Let me know if you need anything else.",
        "Glad I could help! Let me know if there's anything else I can do for you."
    ],
    "apology": [
        "No worries! What can I assist you with?",
        "That's okay! How can I help you?",
        "Apologies are not needed! How can I help you today?",
        "It's all good! What can I do for you?"
    ],
    "funny": [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "Why couldn’t the bicycle stand up by itself? It was two-tired!",
        "I told my computer I needed a break, and now it’s frozen.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ],
    "weather": [
        "The weather today is sunny with a high of 75°F and a low of 55°F. Perfect for outdoor activities!",
        "It looks like it's going to rain today, so don't forget your umbrella!",
        "Currently, it’s partly cloudy with a slight chance of showers in the afternoon.",
        "Expect a cool day with temperatures reaching around 60°F and a light breeze."
    ],
    "time": [
        "The current time is 3:45 PM.",
        "It’s 12:30 PM. Time for lunch!",
        "Right now, it’s 6:00 AM. Early start today!",
        "The time is 9:15 PM. Hope you’re winding down for the day."
    ],
    "reminder": [
        "I can help set reminders for your tasks! What would you like me to remind you about?",
        "Need a reminder? I can set it for you! What should I remind you about?",
        "I can help you remember your appointments. What should I remind you to do?",
        "Tell me what you need a reminder for, and I’ll take care of it!"
    ],
    "math": [
        "What mathematical operation would you like me to perform? Addition, subtraction, multiplication, or division?",
        "I can help with math! What calculation do you need?",
        "Let me know what math problem you want solved!",
        "I'm great with numbers! What do you need help calculating?"
    ],
    "quote": [
        "Here’s an inspiring quote: 'The only way to do great work is to love what you do.' – Steve Jobs",
        "How about this quote: 'The future belongs to those who believe in the beauty of their dreams.' – Eleanor Roosevelt",
        "Here’s something to inspire you: 'Success is not final, failure is not fatal: It is the courage to continue that counts.' – Winston Churchill",
        "Here’s a motivational quote: 'It does not matter how slowly you go as long as you do not stop.' – Confucius"
    ],
    "personal_info": [
        "I'm just a chatbot, so I don't have personal information. But I can help with a lot of other things!",
        "I don’t have personal details, but feel free to ask me anything else.",
        "Sorry, I don’t store personal info. But I can help with your questions or tasks!"
    ],
    "tech_support": [
        "Having an issue? Could you describe your problem in detail so I can help you?",
        "Let’s troubleshoot this! Please provide more details about the issue you're facing.",
        "I’m here for tech support! What seems to be the problem?",
        "I can help with tech issues. Please share more about what you're experiencing."
    ]
}

# Sample user intents
intents = {
    "greeting": ["hi", "hello", "hey", "greetings", "morning", "evening"],
    "goodbye": ["bye", "goodbye", "see you", "later", "take care", "farewell"],
    "help": ["help", "assist", "support", "question", "guide"],
    "gratitude": ["thank you", "thanks", "appreciate it", "grateful"],
    "apology": ["sorry", "apologies", "my bad", "oops"],
    "funny": ["joke", "tell me a joke", "make me laugh"],
    "weather": ["weather", "forecast", "rain", "sunny", "temperature"],
    "time": ["time", "current time", "what time is it", "clock"],
    "reminder": ["reminder", "set reminder", "remind me", "alert"],
    "math": ["add", "subtract", "multiply", "divide", "math", "calculate"],
    "quote": ["quote", "inspire me", "motivational", "wisdom"],
    "personal_info": ["personal", "information", "details"],
    "tech_support": ["issue", "help with", "problem", "tech", "support"]
}

# Basic NLP functions
def preprocess_input(user_input):
    # Tokenize and lemmatize input to make it uniform
    words = nltk.word_tokenize(user_input.lower())
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

def match_intent(user_input):
    # Match user input with predefined intents
    words = preprocess_input(user_input)
    for intent, patterns in intents.items():
        for pattern in patterns:
            if pattern in words:
                return intent
    return None

def chatbot_response(user_input):
    intent = match_intent(user_input)
    
    if intent:
        # Return the most relevant response based on the matched intent
        if intent == "greeting":
            return random.choice(responses["greeting"])
        elif intent == "goodbye":
            return random.choice(responses["goodbye"])
        elif intent == "help":
            return random.choice(responses["help"])
        elif intent == "gratitude":
            return random.choice(responses["gratitude"])
        elif intent == "apology":
            return random.choice(responses["apology"])
        elif intent == "funny":
            return random.choice(responses["funny"])
        elif intent == "weather":
            return random.choice(responses["weather"])
        elif intent == "time":
            return random.choice(responses["time"])
        elif intent == "reminder":
            return random.choice(responses["reminder"])
        elif intent == "math":
            return random.choice(responses["math"])
        elif intent == "quote":
            return random.choice(responses["quote"])
        elif intent == "personal_info":
            return random.choice(responses["personal_info"])
        elif intent == "tech_support":
            return random.choice(responses["tech_support"])
    
    # If no intent matches, use a fallback message
    return "Sorry, I didn't catch that. Could you please rephrase?"

# Main chatbot loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break
    
    print("Bot:", chatbot_response(user_input))
