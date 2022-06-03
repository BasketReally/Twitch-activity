#python script for streaming status
#Basket
#twitch.api,discord.py,requests

#modules
import requests, discord, os, time
from discord.ext import commands

client = commands.Bot(command_prefix='+',self_bot=True) #a client variable





baskets = """
  ______            _        _       
  | ___ \          | |      | |      
  | |_/ / __ _ ___ | | _____| |_ ___ 
  | ___ \/ _` / __ | |/ / _ \ __/ __|
  | |_/ / (_| \__  |   <  __/ |_\__ \

  \____/ \____|___/ _|\_\___|\__|___/\n\n\n
"""

ver = """
 _   _               _               __        _____ 
| | | |             (_)             /  |      |  _  |
| | | | ___ _ __ ___ _  ___  _ __   `| |      | |/' |
| | | |/ _ \ '__/ __| |/ _ \| '_ \   | |      |  /| |
\ \_/ /  __/ |  \__ \ | (_) | | | | _| |_  _  \ |_/ /
 \___/ \___|_|  |___/_|\___/|_| |_| \___/ (_)  \___/ 
"""

global token, tnick

def typing(txt, wait = 0.02):
  #txt = 'текст который нужен'
  for i in txt:  # этот цикл будет брать по 1 буковке из тхт
      time.sleep(wait)
      print(i, end='', flush=True)

with open("config.txt", "r") as file:
  token = file.readline()
  token = str(token)
os.system("clear")
if token == "":
  typing("Ты должен ввести свой токен\n")
  typing("Твой токен только в файле main.py и ты можешь сам посмотреть его код там нету стиллеров и тд\n")
  typing("Если не знаешь как получить свой токен посмотри это видео\n")
  print("https://www.youtube.com/watch?v=uYgkggX_E2g")
  typing("токен должен быть по типу этого - \n Njk4MTM1NzY3NzUwNTQxNDAy.Ycl5sA.kHqhaE9qW9ovTuXvZKZGdLSD0M0\n")
  token = input()

  with open("config.txt", "w") as file:
      file.write(token + "\n")
  
  os.system("clear")
    
typing("Если тебе надо поменять данные то сделать это ты можешь в config.txt!")
time.sleep(3)
os.system("clear")
typing("Каким стримером ты хочешь стать?\n")
tnick = "skauska"
os.system("clear")
typing("Придумай офлайн название\n")
offtitle = input()
os.system("clear")


typing(ver, wait = 0.009)
time.sleep(0.5)
os.system("clear")
  
@client.event
async def on_connect():
  global pr, pf
  pr = 0
  pf = 0
  while True:
    #main funcion
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

    title = data[data.find('title')+9 : data.find("viewer_count")-4]

    debugpr = "name = " + title + "\n" + "Game = "  + game + "\n" + "Viewers = " + viewer_count

    if live == "live":
      if pr == 0:
        typing(baskets)
        typing("[Info] Online status\n")
        time.sleep(0.8)
        typing(debugpr)
        debugprtm = debugpr
        pr = 1
      if pr == 1:
        if debugpr != debugprtm:
          os.system("clear")
          typing(baskets)
          typing("[System] Update!\n")
          typing(debugpr)
          debugprtm = debugpr
    if live == "":
      if pf == 0:
        print("test 2")
        os.system("clear")
        typing(baskets)
        typing("[System] Update!\n")
        time.sleep(0.8)
        typing("[Info] Ofline status\n")
        pf = 1
    if live == "live":
      pf = 0
      
    
    if live == "live":
      #live mode
      activity=discord.Streaming(
        platform = "Twitch",
        application_id = 734420240099704833,
        name = title + "   Viewers : " + viewer_count,
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
        name = offtitle, 
        url = "https://www.twitch.tv/" + tnick)

    await client.change_presence(activity=activity) 


client.run(token, bot=False)
