import requests
import discord
from discord.ext import tasks, commands
import time

while True:
  url = "https://api.twitch.tv/helix/streams?user_login=pwgood"

  req = requests.get(url, headers = {'Authorization' : 'Bearer vl7w8v42mf0p10dphf7uv0xwsc81tp' , 'Client-Id' :  'gp762nuuoqcoxypju8c569th9wz7q5'}, timeout = 15)
  req.raise_for_status()
  info = req.json()
  data = str(info.get('data'))

  game = data[data.find('game_name')+13 :       data.find('type')-4]

  live = data[data.find('type')+8 : data.find('title')-4]

  name = data[data.find('title')+9 : data.find("viewer_count")-4]

  if live == "live":
    print(live)
    print("activity")
    TOKEN ="Njk4MTM1NzY3NzUwNTQxNDAy.Ycl5sA.kHqhaE9qW9ovTuXvZKZGdLSD0M0"
    client = commands.Bot(command_prefix='+',self_bot=True)
    @client.event
    async def on_connect():
      await client.change_presence(activity=discord.Streaming(name = name,game = game, url = "https://www.twitch.tv/pwgood"))
    print("pre stream")
    print("stream")
    client.run((TOKEN), bot=False)
  if live == "":
    print(live)
    print("activity  sleep")
    TOKEN ="Njk4MTM1NzY3NzUwNTQxNDAy.Ycl5sA.kHqhaE9qW9ovTuXvZKZGdLSD0M0"
    client = commands.Bot(command_prefix='+',self_bot=True)
    @client.event
    async def on_connect():
      await client.change_presence(activity=discord.Streaming(name = "Sleeping", url = "https://www.twitch.tv/pwgood"))
    print("pre stream")
    print("non stream")
    client.run((TOKEN), bot=False)
  time.sleep(15)
