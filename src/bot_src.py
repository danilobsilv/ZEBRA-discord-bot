import discord 
import re 

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
    formated_message_author = re.sub("^#\d{1,10}$", "" , message.author.name)
    
    # treat the variations of the same word 
    message_content = message.content
    lower_message_content  = message_content.lower()

    if message.author == client.user:
        return 

    responses = {
        "#oi": f"Oi, {formated_message_author}, tudo bem?",
        "#danilo": "Danilo está ocupado me desenvolvendo...Para de encher o saco!",
        "#fernanda": "Fernanda é a mãe dele!",
        # "#kkk": any_def_Iwant() it works 
    }

    for keyword, response in responses.items():
        if lower_message_content.startswith(keyword):
            await message.channel.send(response)
            break



