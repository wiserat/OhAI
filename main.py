#!/usr/bin/env python3

from chainchat import chat
from ohbot import * # Import the modified ohbot library
from recognize import recognize
import sys

def main():
    lang = sys.argv[-1] # Get the language
    if lang == "cs":
        prompt = recognize("Davide", lang)
        prompt += " Say the answer in Czech"
    elif lang == "en":
        prompt = recognize("David", lang)
    print(prompt)
    answer = chat(prompt) # Generate the response from the user
    print(answer) # Print the answer for debuging lol
    say(answer, lang) # Make the ohbot talk

if __name__ == "__main__":
    main()