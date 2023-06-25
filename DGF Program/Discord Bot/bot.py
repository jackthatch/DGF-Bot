import discord

client = discord.Client()

TOKEN = "MTA3NzM4OTcwNDgyMDk1MzE5OA.GN2UYM.DHZiUvEnTxDu6NoCfLBmcj3ECtFHexD63U6p24"

async def send_message(message):        ##Pass in our SMS message
    channel = client.get_channel()
    await channel.send(message)