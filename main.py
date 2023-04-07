#!/usr/bin/env python3

from chat import conversaton_handler # Import the function that talks with gpt-3.5-turbo
from ohbot import * # Import the modified ohbot library
import sys

def main():
    lang = sys.argv[-1] # Get the language
    prompt = input("User: ") # This will be used to generate the response for the user
    answer = conversaton_handler(prompt) # Generate the response from the user
    print(answer) # Print the answer for debuging lol
    say(answer, lang, soundDelay=0.1) # Make the ohbot talk

if __name__ == "__main__":
    main()