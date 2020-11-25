#import Discord Package
import discord
from discord.ext import commands
import emoji
import pandas as pd
import random
import praw

reddit = praw.Reddit(client_id = "#",
                     client_secret = "#",
                     username="#",password="#",
                     user_agent= "pythonpraw")


#Client (for the bot)
client = commands.Bot(command_prefix="=-", help_command=None)

@client.command(name="help")
async def help(ctx):
    #helptext = "```"
    helptext = "--- list of all the commands --- \n"
    for command in client.commands:
        helptext+=f"{command}\n"
    #helptext+="```"
    await ctx.send(helptext)


@client.command(name = 'version')
async def version(context):
    general_channel = client.get_channel(781098734036451330)
    myEmbed = discord.Embed(title = "About me", description="Bot using python >:-)", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value = "21st November 2020", inline=False)
    myEmbed.set_footer(text="Type -/help to know more :)")
    myEmbed.set_author(name="~~~ name ~~~")
    #await general_channel.send(embed=myEmbed)
    await general_channel.send(embed=myEmbed)


@client.command(name = 'memes')
async def meme(context):
    general_channel = client.get_channel(781098734036451330)
    subreddit = reddit.subreddit("memes")
    all_subs = []

    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    meme = discord.Embed(title = name)

    meme.set_image(url =url)

    await general_channel.send(embed=meme)

@client.command(name = 'random_images')
async def meme(context):
    general_channel = client.get_channel(781098734036451330)
    subreddit = reddit.subreddit("images")
    all_subs = []

    top = subreddit.top(limit = 1000)

    for submission in top:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    pic = discord.Embed(title = name)

    pic.set_image(url =url)

    await general_channel.send(embed=pic)
)


# Run the client on the server
client.run('#')
