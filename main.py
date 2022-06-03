#python script for streaming status
#Basket
#twitch.api,discord.py,requests

#modules
import requests, discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='+',self_bot=True) #a client variable

#global debug
#debug = input("Enable debug mode?(Yes/No)? : ")

  
@client.event
async def on_connect():
  while True:
    #main funcion
    tnick = "pwgood" #a name variable. Type a twitch user here
    url = "https://api.twitch.tv/helix/streams?user_login=" + tnick

    headers = {
      'Authorization' : 'Bearer vl7w8v42mf0p10dphf7uv0xwsc81tp', 
      'Client-Id' :  'gp762nuuoqcoxypju8c569th9wz7q5'
    }

    req = requests.get(url, headers = headers, timeout = 15)#get request to twitch api
  
    req.raise_for_status()
    info = req.json()
    data = str(info.get('data'))
  

    game = data[data.find('game_name')+13 :       data.find('type')-4]

    live = data[data.find('type')+8 : data.find('title')-4]

    viewer_count = str(data[data.find('viewer_count')+15 : data.find("started_at")-3])

    title = data[data.find('title')+9 : data.find("viewer_count")-4] + "   Viewers : " + viewer_count

    debugpr = "name = " + title + "," + "Game = " + "," + game + "Viewers = " + viewer_count

    global pr, pf
    pr, pf = 0

    if live == "live":
      if pr == 0:
        print(debugpr)
        debugprtm = debugpr
        pr = 1
      if pr  == 1:
        if debugpr != debugprtm:
          os.system("clear")
          print("UPDATE!")
          print(debugpr)
          debugprtm = debugpr
    if live == "":
      if pf == 0:
        os.system("clear")
        print("UPDATE!")
        print("sleep")
        pf = 1
    if live == "live":
      pf = 0
      
    
    if live == "live":
      #live mode
      activity=discord.Streaming(
        platform = "Twitch",
        application_id = 734420240099704833,
        name = title,
        game = game, 
        assets = {
          'twitch' : 'pwgood',
          'large_image' : '_'
        },
        url = "https://www.twitch.tv/" + tnick
      )
      
    
    if live == "":
      #ofline mode
      activity=discord.Streaming(
        name = "Играю в шарарам | Приватный стрим", 
        url = "https://www.twitch.tv/" + tnick)

    await client.change_presence(activity=activity) 

print("version 0.7")


client.run("token", bot=False)
