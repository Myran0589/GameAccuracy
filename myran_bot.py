import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import colorsys

client = commands.Bot(command_prefix='?')


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("============")
    print("Made By Myran#0001")

@client.command()
async def hq(ctx,time=None, accuracy=None, ques=None, prize=None):
	if not time or not accuracy or not ques or not prize:
		await ctx.say("wrong use! please add correct values")
	else:
		embed=discord.Embed(color=discord.Color.red())
		embed.add_field(name="Hq Trivia",value="Results of Hq Trivia")
		embed.add_field(name="Game Time",value=time)
		embed.add_field(name="Accuracy",value=accuracy)
		embed.add_field(name="Total Question",value=ques)
		embed.add_field(name="Winning amount",value=prize)
		embed.set_footer(text="Made by Myran#0001")
		embed.set_thumbnail(url="") //Put Your Thumbnail url
		await ctx.send(embed=embed)
			

client.run('Token')
