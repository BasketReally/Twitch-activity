import requests
import discord
from discord.ext import tasks, commands

while True:
  url = "https://api.twitch.tv/helix/streams?user_login=pwgood"

  req = requests.get(url, headers = {'Authorization' : 'Bearer vl7w8v42mf0p10dphf7uv0xwsc81tp' , 'Client-Id' :  'gp762nuuoqcoxypju8c569th9wz7q5'}, timeout = 15)
  req.raise_for_status()
  info = str(req.json())
  type = info.find("live")
  if type > 0:
    TOKEN ="Njk4MTM1NzY3NzUwNTQxNDAy.Ycl5sA.kHqhaE9qW9ovTuXvZKZGdLSD0M0"
    client = commands.Bot(
      command_prefix='+',
      self_bot=True
    )
    @client.event
    async def on_connect():
      await client.change_presence(activity =   discord.Streaming(name = "Basket client coding", url = "https://www.twitch.tv/pwgood"))
    client.run((TOKEN), bot=False)
