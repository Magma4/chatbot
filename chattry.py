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

# Load intents data from JSON file
intents = json.loads(open('intents.json').read())

# Load preprocessed words and classes from pickle files
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Load pre-trained chatbot model
model = load_model('chatbotmodel.h5')

# Function to clean up a sentence by tokenizing and lemmatizing
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

# Function to convert a sentence to a bag of words representation
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    # Return only the first 53 elements (consistent with your model input shape)
    return np.array(bag)

# Function to predict the intent of a given sentence
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Function to get a random response based on the predicted intent
def get_response(ints, intents):
    try:
        # Assuming ints is a list
        tag = ints[0]['intent']
        intent = next((item for item in intents['intents'] if item['tag'] == tag), None)
        if intent:
            response = intent['responses']
            return random.choice(response)
        else:
            return "I'm sorry, I didn't understand that."
    except IndexError:
        # Handle the case where the list is empty
        return "I'm sorry, I didn't understand that."

# Function to greet the user
def greetings():
    """This function let's the bot greets the user when started"""
    # Get the current hour
    hour = dt.datetime.now().hour
    # Greet the user based on the time of day
    if hour >= 6 and hour <= 12:
        print("Good morning")
    elif hour >= 12 and hour <= 18:
        print("Good afternoon")
    elif hour >= 18 and hour <= 24:
        print("Good evening")
    else:
        print("Good night")
    print("My name is Chatbot.")  
    print("How can i help you?")

# Uncomment the following line to print the initial greeting

# Call the greetings function to greet the user initially
greetings()


# Main loop to receive user input and provide responses
while True:
    # Get user input
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
