import discord
import random
import unidecode

client = discord.Client()
lastChannel = None
lastAuthor = None

def insulte_in_message(content):
    insultes = open('./insultes.txt', encoding="utf-8").read().splitlines()

    for word in content.split():
        if unidecode.unidecode(word).lower() in insultes:
            return True
    return False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    lastChannel = message.channel
    lastAuthor = message.author
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        quotes = open('./quotes.txt', encoding="utf-8").readlines();
        quote = quotes[random.randint(0, len(quotes) - 1)]
        await message.channel.send(f"{message.author.mention} {quote}")
        return

    if insulte_in_message(message.content):
        warnings = open('./quotes.txt', encoding="utf-8").readlines();
        warning = warnings[random.randint(0, len(warnings) - 1)]
        await message.channel.send(f"{message.author.mention} {warning}")
        return

tokenFile = open('./token')
token = tokenFile.readlines()[0]

client.run("NjI2OTAxODYzNjAxNjY4MTA2.XY05aQ.FNj1AxXE2n9yuo3ZxvLswh-ja7Q")
