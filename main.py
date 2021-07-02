import discord
import os
import requests
import json
import random

from replit import db
from keep_alive import keep_alive

client = discord.Client()
my_secret = os.environ['TOKEN']

swear_words = ["Fuck","Shit","Dick"]

starter_encouragements = [
  "Yoooo!",
  "Bismelleh",
  "Mashallah"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith('.dhelp'):
    await message.channel.send('The help command is a WIP')

  if msg.startswith('.dinspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options.extend(db["encouragements"][:])

    if any(word in msg for word in swear_words):
      await message.channel.send(random.choice(options))

  if msg.startswith(".dnew"):
    encouraging_message = msg.split(".dnew ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith(".ddel"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split(".ddel", 1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith(".dlist"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith(".dresponding"):
    value = msg.split(".dresponding ", 1)[1]
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on")
    elif value.lower() == "false":
      db["responding"] = False
      await message.channel.send("Responding is off")
    else:
      await message.channel.send("I have no idea what you just said...")

keep_alive()
client.run(my_secret)