import random
import json
import torch
from speak import say
from listen import Listen
from skills import NonInputExecution,InputExecution

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda'if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
     intents = json.load(json_data)
FILE = "processor.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Adhvika"
print("hey i'm Adhvika let's talk")
say("hey iam adhvika let's talk")
while True:

    sentence = Listen()
    result = str(sentence)
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]: 
                reply = (f" {random.choice(intent['responses'])}")

                if "time" in reply:
                    NonInputExecution(reply)

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "wikipedia" in reply:
                    InputExecution(reply,sentence)

                elif "google" in reply:
                    InputExecution(reply,result)

                elif "whatsapp" in reply:
                    InputExecution(reply,sentence)

                elif "email" in reply:
                    InputExecution(reply,sentence)

                elif "youtube" in reply:
                    InputExecution(reply,sentence)

                else:
                  say(reply)

    

            