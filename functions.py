from twilio.rest import Client
import os

#Function to get sensitive information
def load_tokens(file_path="token.txt"):
    tokens = {}
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            tokens[key] = value
    return tokens

#Whatsapp function
def send_whatsapp_messages(numbers, message, account_sid, auth_token, twilio_whatsapp_number):
    client = Client(account_sid, auth_token)
    for number in numbers:
        client.messages.create(
            from_=twilio_whatsapp_number,
            body=message,
            to=f'whatsapp:{number.strip()}'
        )