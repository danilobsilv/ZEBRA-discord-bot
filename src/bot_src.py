import discord 
import re 
# from tokens import Tokens
# from utils.functions.functions import *

# token = Tokens()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# def printarOi():
#     return "Hello World!"
@client.event
async def on_ready():
    print(f"{client.user} is online!")

@client.event
async def on_message(message):
    formated_message_author = re.sub("^#\d{1,10}$", "" , message.author.name)

    if message.author == client.user:
        return 
    
    if message.content.startswith("#oi"):
        # await message.channel.send(printar_oi()) 
        await message.channel.send(f"Oi, {formated_message_author}, tudo bem?")

 
# client.run(token.bot_token)

