# Import necessary libraries
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import datetime as dt
from tensorflow.keras.models import load_model

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents, words, classes, and model at startup
with open('chatbot/intents.json') as file:
    intents = json.load(file)

words = pickle.load(open('chatbot/words.pkl', 'rb'))
classes = pickle.load(open('chatbot/classes.pkl', 'rb'))
model = load_model('chatbot/chatbotmodel.h5')

# Function to clean and lemmatize a sentence
def clean_and_lemmatize(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word) for word in sentence_words]

# Function to create a bag of words from a sentence
def create_bag_of_words(sentence):
    sentence_words = clean_and_lemmatize(sentence)
    bag = [0] * len(words)
    for word in sentence_words:
        if word in words:
            bag[words.index(word)] = 1
    return np.array(bag)

# Function to predict the class (intent) of a sentence
def predict_intent(sentence):
    bow = create_bag_of_words(sentence)
    predictions = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    return [{'intent': classes[i], 'probability': str(probability)} 
            for i, probability in enumerate(predictions) if probability > ERROR_THRESHOLD]

# Function to get a random response for the predicted intent
def get_response(predicted_intents):
    if predicted_intents:
        tag = predicted_intents[0]['intent']
        for intent in intents['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that."

# Function to greet the user based on the time of day
def greet_user():
    current_hour = dt.datetime.now().hour
    if 6 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    elif 18 <= current_hour <= 24:
        greeting = "Good evening"
    else:
        greeting = "Good night"
    print(f"{greeting}, my name is Chatbot. How can I help you?")

# Greet the user initially
greet_user()

# Main loop for receiving user input and responding
while True:
    user_input = input("You: ")
    predicted_intents = predict_intent(user_input)
    response = get_response(predicted_intents)
    print("Chatbot: " + response)
