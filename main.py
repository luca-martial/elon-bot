import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

TOXIC_API_URL = "https://api-inference.huggingface.co/models/unitary/multilingual-toxic-xlm-roberta"

ELON_API_URL = "https://api-inference.huggingface.co/models/luca-martial/DialoGPT-Elon"

headers = {"Authorization": f"Bearer {os.environ['HUGGING_FACE_API']}"}

# create querying function for toxicity score API
def query(payload):
  data = json.dumps(payload)
  response = requests.request("POST", TOXIC_API_URL, headers=headers, data=data)
  score_result = json.loads(response.content.decode("utf-8"))
  toxic_list = score_result[0]
  toxic_dict = toxic_list[0]
  toxic_score = toxic_dict['score']
  return toxic_score

# create querying function for elon conversation API
def query_convo(payload):
  data = json.dumps(payload)
  response = requests.request("POST", ELON_API_URL, headers=headers, data=data)
  elon_convo = json.loads(response.content.decode("utf-8"))
  return elon_convo

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  # query APIs
  query({"inputs": 'toxic test'})
  query_convo({'inputs': {'text': 'convo test'}})

@client.event
async def on_message(message):
  msg = message.content
  usr = message.author

  # prevent responding to its own messages
  if usr == client.user:
    return

  # track number of toxic comments for each user
  if str(usr) not in db.keys():
    db[str(usr)] = 0

  # create ability to check how many toxic comments user has sent
  if msg.startswith("!strikes"):
    await message.channel.send("You've got " + str(db[str(usr)]) +  "strike(s) so far.")
    return
  
  # create specific reply whenever bitcoin is mentioned
  if 'bitcoin' in msg.lower():
    async with message.channel.typing():
      await message.channel.send("Have you not heard? \nhttps://twitter.com/elonmusk/status/1392602041025843203")
      return

   # create specific reply whenever dogecoin is mentioned
  if 'dogecoin' in msg.lower():
    async with message.channel.typing():
      await message.add_reaction('🚀')
      await message.channel.send("To the mooooonnn!!")
      return

  # evaluate toxicity of user's message and track strikes
  if query({"inputs": msg}) > 0.75:
    if db[str(usr)] == 0:
      db[str(usr)] += 1
      await message.add_reaction('😠')
      await message.channel.send("Watch your language! The rule is three strikes and you're out.")
    elif db[str(usr)] == 1:
      db[str(usr)] += 1
      await message.add_reaction('😡')
      await message.channel.send("Watch your language! One more strike and you're out.")
    elif db[str(usr)] == 2:
      # kick user out on third strike
      await usr.kick()
      del db[str(usr)]
      await message.channel.send(f'I just kicked {str(usr)} out. Behave yourselves.')

  else:
    # let users know bot is typing
    async with message.channel.typing():
      # query elon conversational API with user's message as input
      response = query_convo({'inputs': {'text': msg}})
      elon_response = response.get('generated_text', None)

    # error message
    if not elon_response:
      elon_response = "Hmm... This doesn't happen often, but I think my brain has overheated. Say that again please."

    await message.channel.send(elon_response)

keep_alive()

client.run(os.environ['TOKEN'])