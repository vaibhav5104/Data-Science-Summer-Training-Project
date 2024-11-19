import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import requests

# Predefined responses
RESPONSES = {
    "greeting": ["Hi there!", "Hello!", "Hey!", "Hi! How can I assist you?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure I understand. Can you rephrase?", "Sorry, I didn't get that."]
}

# Define functions for specific tasks
def get_joke():
    """Fetches a random joke from an API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = response.json()
        return f"{joke['setup']} ... {joke['punchline']}"
    except Exception as e:
        return "I couldn't fetch a joke at the moment. Try again later!"

def get_weather(city):
    """Fetches weather data for a given city."""
    api_key = "your_openweather_api_key_here"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return "I couldn't find the weather for that location."
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"The current temperature in {city} is {temp}°C with {weather}."
    except Exception as e:
        return "I couldn't fetch the weather data. Please try again later."

# Match user input with intents
def match_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return "farewell"
    elif "joke" in tokens:
        return "joke"
    elif "weather" in tokens:
        return "weather"
    return "default"

# Chatbot function
def chatbot():
    print("Chatbot: Hi! I am your advanced chatbot. Ask me anything or type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["exit", "quit"]:
            print(random.choice(RESPONSES["farewell"]))
            break
        
        intent = match_intent(user_input)
        
        if intent == "greeting":
            print("Chatbot:", random.choice(RESPONSES["greeting"]))
        elif intent == "farewell":
            print("Chatbot:", random.choice(RESPONSES["farewell"]))
            break
        elif intent == "joke":
            print("Chatbot:", get_joke())
        elif intent == "weather":
            print("Chatbot: Please provide a city name.")
            city = input("You: ")
            print("Chatbot:", get_weather(city))
        else:
            print("Chatbot:", random.choice(RESPONSES["default"]))

# Run the chatbot
if __name__ == "__main__":
    chatbot()
