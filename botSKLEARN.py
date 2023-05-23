# ****************************************
# Authors:
# - Diego Cordova
# - Cristian Aguirre
# Discord bot functionality
# ****************************************

# Libraries
import discord as ds
import os
from random import randint
from AnalizerSKLEARN import SentimentAnalizer

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Cliente de discord
intents: ds.Intents = ds.Intents.default()
intents.message_content = True
client = ds.Client(intents=intents)

# Support messages Dabasase
support_msg = [
    "Hey there! I noticed you're feeling down, but remember that tough times don't last forever. You're stronger than you think!",
    "I'm sorry to hear that you're feeling low. Just know that you're not alone, and there are people who care about you. Reach out if you need someone to talk to.",
    "I understand that things might be challenging right now, but remember that every storm eventually passes. Stay strong and believe in yourself.",
    "I'm here to remind you that you're capable of overcoming anything that comes your way. Keep pushing forward and don't give up.",
    "I know it's tough, but try to focus on the positive aspects of your life. You have so much strength within you, and better days are ahead.",
    "Sending you a virtual hug and some words of encouragement. You're resilient and have the power to rise above any obstacles. You got this!",
    "Remember that setbacks are just temporary. Use this experience to grow and learn. You're on a journey of self-discovery, and brighter days are coming.",
    "Sometimes life can be challenging, but it's during these difficult times that you discover your true strength. Keep your head up and keep moving forward.",
    "I'm sorry to hear that you're feeling down, but know that you're important and valued. Take some time for self-care and reach out to loved ones for support.",
    "Just a friendly reminder that you're not defined by your circumstances. You have incredible potential, and I believe in your ability to overcome any obstacles that come your way.",
    "I know it may feel overwhelming right now, but remember that every challenge is an opportunity for growth. You have the strength to overcome this!",
    "I'm sorry to hear that things aren't going well. Just know that setbacks are temporary, and you have the resilience to bounce back stronger than ever.",
    "During tough times, it's important to be kind to yourself. Remember to practice self-care and reach out to your support system. You don't have to face this alone.",
    "I understand that things seem tough right now, but remember that you've overcome obstacles before. Trust in your abilities and keep moving forward.",
    "Sending you positive vibes and a gentle reminder that you're not defined by your circumstances. Your worth and potential are limitless.",
    "I'm here to remind you that you're not alone in your struggles. Reach out to someone you trust for support, and remember that brighter days are ahead.",
    "Even in the darkest moments, there's always a glimmer of hope. Hold on to that hope and know that better days are on the horizon.",
    "I know it's hard, but try to shift your focus towards gratitude and the things that bring you joy. Sometimes a change in perspective can make all the difference.",
    "Don't underestimate your own strength. You've faced challenges before and emerged stronger. Trust in yourself and your ability to overcome this.",
    "Remember, you're not defined by your past or your current circumstances. You have the power to create a brighter future. Keep pushing forward!",
]

help_string = '''
Hello!! I'm Emotion-Sense 🤖.
My purpose in existence is to use artificial intelligence
for text sentiment analysis and detect messages with high
levels of sadness or anger.

If I detect a message with these characteristics, I will send a direct message
to the sender.

My creators are:
🤓Diego Córdova and 🤓Cristian Aguirre
'''

# lOGIN


@client.event
async def on_ready():
    print(f"Bot online as {client.user}")

# ---------------------------- Commmands -----------------------

# Comandos de texto


Analizer = SentimentAnalizer()


async def handle_dm(msg: ds.Message):

    if msg.content == '-cat':
        await msg.author.dm_channel.send(file=ds.File('cat.jpeg'))


async def get_supportMSG() -> str:
    string = support_msg[randint(0, len(support_msg) - 1)]
    string += '\nI can send you an image of a cat to cheer you up\nJust enter command "-cat"'
    return string


@client.event
async def on_message(msg: ds.Message):
    '''Ejecuta el comando ingresado o devuelve mensaje de error'''

    if msg.author == client.user:
        return

    # Handle dm messages
    if isinstance(msg.channel, ds.channel.DMChannel):
        await handle_dm(msg)
        # text message
    text_msg = msg.content

    # Comando que envia mensaje si es jueves
    if text_msg == '-help':
        emb: ds.Embed = ds.Embed(
            title='Emotion-Sense',
            color=ds.Color.blue(),
            description=help_string,
        )
        # await msg.reply(embed=emb)
        await msg.channel.send(embed=emb)
        return

    respuesta = Analizer.find_sentiment(text_msg)

    if respuesta == 'negative':
        emb: ds.Embed = ds.Embed(
            title='I have detected negative emotions in your last message',
            color=ds.Color.blue(),
            description=await get_supportMSG()
        )
        # Creates dm channel with author if not exists
        try:
            await msg.author.create_dm()
        except:
            pass

        # Sends dm to author
        await msg.author.dm_channel.send(embed=emb)

    return

# Al unirse alguien al servidor


@client.event
async def on_member_join(member: ds.Member):
    emb: ds.Embed = ds.Embed(
        title='Emotion-Sense',
        color=ds.Color.blue(),
        description=help_string,
    )
    await member.create_dm()
    await member.dm_channel.send(embed=emb)

# ---------------------------- Funcionalidad -----------------------

App_Token = os.getenv("TOKEN")
client.run(App_Token)  # Corre en discord
