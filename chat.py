# This is for now using GPT-3.5-turbo whiich will be changed for something else

import openai # Using the openai library instead of just making a request, subject to change

openai.api_key_path = ".env" # Get the key from the .env file
model_engine = "gpt-3.5-turbo-0301" # Choose model


def chat_query(prompt): # Make request with the openai library
    completions = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50, # This has been lowered for speed reasons
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].message.content # Get the string
    return message # Return the string

def conversaton_handler(prompt): # Return the genrated response
    response = chat_query(prompt)
    return response
