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

global token, tnick, pr, pf

def typing(txt, wait = 0.02):
  #Функция для эффекта печатающегося текста
  for i in txt:
      time.sleep(wait)
      print(i, end='', flush=True)

with open("config.txt", "r") as file:
  #Чтение конфига
  token = file.readline()
  token = str(token)
os.system("cls||clear") #Очищение консоли
if token == "":
  #Узнавание токена
  typing("Ты должен ввести свой токен\n")
  typing("Твой токен только в файле main.py и ты можешь сам посмотреть его код там нету стиллеров и тд ведь я закомментировал даже time.sleep\n")
  typing("Если не знаешь как получить свой токен посмотри это видео\n")
  print("https://www.youtube.com/watch?v=uYgkggX_E2g")
  typing("токен должен быть по типу этого - \n Njk4MTM1NzY3NzUwNTQxNDAy.Ycl5sA.kHqhaE9qW9ovTuXvZKZGdLSD0M0\n")
  token = input()

  with open("config.txt", "w") as file:
    #Запись в конфиг
      file.write(token + "\n")
  
  os.system("cls||clear") #Очищение консоли
    
typing("[Warning] Если тебе надо поменять данные то сделать это ты можешь в config.txt!")
time.sleep(3) #Задержка
os.system("cls||clear") #Очищение консоли
typing("Каким стримером ты хочешь стать?\n")
tnick = input()
os.system("cls||clear") #Очищение консоли
typing("Придумай офлайн название\n")
offtitle = input()
os.system("cls||clear") #Очищение консоли


typing(ver, wait = 0.009)
time.sleep(0.5)
os.system("cls||clear") #Очищение консоли
  
@client.event
async def on_connect():
  #Функция которая срабатывает при запуске скрипта
  pr = 0
  pf = 0
  while True:
    url = "https://api.twitch.tv/helix/streams?user_login=" + tnick #Ссылка апи твича

    headers = {
      'Authorization' : 'Bearer vl7w8v42mf0p10dphf7uv0xwsc81tp', 
      'Client-Id' :  'gp762nuuoqcoxypju8c569th9wz7q5'
    } #Заголовки для апи твича

    req = requests.get(url, headers = headers, timeout = 15)#get request to twitch api
  
    req.raise_for_status()
    info = req.json()
    data = str(info.get('data'))
  

    game = data[data.find('game_name')+13 :       data.find('type')-4] #Переменая с игрой стримера

    live = data[data.find('type')+8 : data.find('title')-4] #Переменная с типом стрима

    viewer_count = str(data[data.find('viewer_count')+15 : data.find("started_at")-3]) #Перменная с счетчиком зрителей

    title = data[data.find('title')+9 : data.find("viewer_count")-4] #Название стрима

    debugpr = "name = " + title + "\n" + "Game = "  + game + "\n" + "Viewers = " + viewer_count + "\n" + "Streamer name = " + tnick #Вся основная информация о стриме

    if live == "live":
      #Я не вижу смысла объяснять вам все это т.к. вы и так не поймете но это чтобы спамило в консоль данными
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
      #режим стрима
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
      #офлайн режим
      activity=discord.Streaming(
        name = offtitle, 
        url = "https://www.twitch.tv/" + tnick)

    await client.change_presence(activity=activity) #Смена статуса

#Запуск стрима
client.run(token, bot=False)
