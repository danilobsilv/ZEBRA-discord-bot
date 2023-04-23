import discord 
import re 
import json
from utils.functions.functions import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} is online!")


'''
the function is triggered whenever a new message is sent in a channel where the bot is present. 
It verifies if the message begins with any of the predefined keywords in the responses dictionary, and if it does, 
sends an appropriate response to the message channel.
'''
@client.event
async def on_message(message):
    
    # treat the variations of the same word 
    message_content = message.content
    lower_message_content  = message_content.lower()

    if message.author == client.user:
        return 

    with open("config\keywords.json", "r") as keywords_file:
        data = json.load(keywords_file)

    for pair in data["keywords"]:
        trigger = pair["trigger"]
        response = pair["response"]

        if lower_message_content.startswith(trigger):
            response_function = eval(response)
            await message.channel.send(response_function)
