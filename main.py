import discord
import os

from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = ".d")
token = os.environ['TOKEN']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
  print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
  print('{member} has left a server')

@client.command()
async def ping(ctx):
  await ctx.send(f"Latency is {round(client.latency * 1000)}ms")

@client.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount+1)

keep_alive()
client.run(token)