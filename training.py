import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

# nltk.download('punkt')
# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents from JSON file
intents = json.loads(open('intents.json').read())

# Initialize lists to store words, classes, and documents
words = []
classes = []
documents = []
# Define a list of characters to be ignored
ignore_letters = ['?', '!', '.', ',']

# Iterate through each intent and pattern to preprocess the data
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each pattern into words
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # Create a tuple with the tokenized words and the intent tag
        documents.append((word_list, intent['tag']))
        # Add the intent tag to the classes list if not already present
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize words and remove characters to ignore
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
# Sort and remove duplicates from the words list
words = sorted(set(words))

# Sort and remove duplicates from the classes list
classes = sorted(set(classes))

# Save preprocessed words and classes using pickle
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Initialize lists for training data and output
training = []
output_empty = [0] * len(classes)

# Convert documents into bag of words and one-hot encoded output
for document in documents:
    bag = np.zeros(len(words), dtype=int)

    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    for word in word_patterns:
        if word in words:
            bag[words.index(word)] = 1

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

# Shuffle the training data
random.shuffle(training)

# Convert training data and output to NumPy arrays
train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])

# Build a neural network model using Keras
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5)) 
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model using stochastic gradient descent optimizer
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save the trained model
model.save('chatbotmodel.h5', hist)
print("Done")
