#import Discord Package
import discord
from discord.ext import commands

#Client (for the bot)
client = discord.Client()


@client.event
async def on_message(message):
    
    if message.content == 'Hello':
        general_channel = client.get_channel('#')
        await general_channel.send('I am here!')

    elif message.content == '>version':
        general_channel = client.get_channel('#')
        myEmbed = discord.Embed(title = "About me", description="Bot using python >:-)", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value = "21st November 2020", inline=False)
        myEmbed.set_footer(text="PS: I am amazing")
        myEmbed.set_author(name="~~~ name ~~~")
        await general_channel.send(embed=myEmbed)

# Run the client on the server
client.run('#')
 
