# ****************************************
# Authors:
# - Diego Cordova
# - Cristian Aguirre
# Discord bot functionality
# ****************************************

# Libraries
import discord as ds
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Cliente de discord
intents: ds.Intents = ds.Intents.default()
intents.message_content = True
client = ds.Client(intents=intents)

help_string = '''
Hola!!, soy Emotion-Sense🤖.
Mi propósito en la existencia es utilizar inteligencia artificial
para analisis de sentimiento de texto y detectar mensajes con alta
carga de Trizesa, enojo o felicidad.

En caso detecte un mensaje con estas características, enviaré un dm
al emisor.

Mis creadores son:
🤓Diego Córdova y 🤓Cristian Aguirre 
'''

# lOGIN


@client.event
async def on_ready():
    print(f"Bot online as {client.user}")

# ---------------------------- Commmands -----------------------

# Comandos de texto


@client.event
async def on_message(msg: ds.Message):
    '''Ejecuta el comando ingresado o devuelve mensaje de error'''

    if msg.author == client.user:
        return

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

    # TODO procesar texto con IA

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
