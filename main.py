import discord
from discord.ext import commands
import asyncio

bot_prefix = "" # The prefix for all of your bots commands

bot_token = "" # Get your bots token from the Discord developer portal

client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all()) # Defines the bot

# Make sure all of the intents are enabled from the Discord developer portal

########################################################

# Sample events and commands

@client.event # client.event does not need to be called
async def on_ready(): # Tells you when the bot is online
    print(f"{client.user} is online!")

@client.command() # client.command must be called
async def ping(ctx): # Pass the ctx paramater so you can reply to the message and get information about the message
    await ctx.reply("Pong!") # Replying to the message

########################################################

# Now we are going to make a command to say something after waiting a given amount of time

@client.command()
async def delayed_response(ctx, *, delay=None): 
    if delay == None: # Makes sure that the user provided an amount to delay
        await ctx.reply("Please give me a time to wait!")
    else:
        try: # Checks if the delay given is a number
            delay = int(delay)
            await asyncio.sleep(delay)
            await ctx.reply(f"I waited **{delay}** seconds before replying!")
        except:
            await ctx.reply("You need to give me a number only!")

client.run(bot_token)
