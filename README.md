# Adhvika-Ai-conversational-bot-using-NLP
Adhvika is a conversational ai bot made using Natural language processing (NLP).  It was developed by versatiledvkr in the year 2021 .
Pytorch & nltk(natural language toolkit) these are the frameworks used in making Adhvika . 

The implementation should be easy to follow for beginners and provide a basic understanding Adhvika.
The implementation is straightforward with a Feed Forward Neural net with 2 hidden layers.
Customization for your own use case is super easy. Just modify intents.json with possible patterns and responses and re-run the training (see below for more info)

Installation

Create an environment
Whatever you prefer (e.g. conda or venv)

mkdir myproject

$ cd myproject
$ python3 -m venv venv
Activate it
Mac / Linux:

. venv/bin/activate
Windows:

venv\Scripts\activate

Install PyTorch and dependencies
For Installation of PyTorch see official website.

You also need nltk:

pip install nltk
If you get an error during the first run, you also need to install nltk.tokenize.punkt: Run this once in your terminal:

$ python
>>> import nltk
>>> nltk.download('punkt')
Usage
Run

python train.py
This will dump BRAIN.pth file. And then run

python conversational bot.py
Customize
Have a look at intents.json. You can customize it according to your own use case. Just define a new tag, possible patterns, and possible responses for the Adhvika. You have to re-run the training whenever this file is modified.

{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    ...
  ]
}
