import discord


from discord.ext import tasks, commands

TOKEN = "Njk4MTM1NzY3NzUwNTQxNDAy.Ycl5sA.kHqhaE9qW9ovTuXvZKZGdLSD0M0"
client = commands.Bot(
  command_prefix='+',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "Basket client coding", url = "https://www.twitch.tv/pwgood"))



client.run((TOKEN), bot=False)
