import discord
import os
import js2py

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members= True
client = discord.Client(intents=intents)
token = os.environ['TOKEN']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 909089626910752839:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    if payload.emoji.name == 'globe_with_meridians':
      role = discord.utils.get(guild.roles, name='Portfolio Website Viewer')
    elif payload.emoji.name == 'robot':
      role = discord.utils.get(guild.roles, name='Spu.D Bot Viewer')
    elif payload.emoji.name == 'the_potato_pack':
      role = discord.utils.get(guild.roles, name='The Potato Pack Viewer')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)
    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.add_roles(role)
        print("done")
      else:
        print("Member not found")
    else:
      print("Role not found")

@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if message_id == 909089626910752839:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    if payload.emoji.name == 'globe_with_meridians':
      role = discord.utils.get(guild.roles, name='Portfolio Website Viewer')
    elif payload.emoji.name == 'robot':
      role = discord.utils.get(guild.roles, name='Spu.D Bot Viewer')
    elif payload.emoji.name == 'the_potato_pack':
      role = discord.utils.get(guild.roles, name='The Potato Pack Viewer')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)
    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.remove_roles(role)
        print("done")
      else:
        print("Member not found")
    else:
      print("Role not found")

keep_alive()
client.run(token)