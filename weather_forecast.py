import requests
import re
from datetime import datetime
import time
import pygame

# 山口市の cityコード
city_code = "350020" 
# weather.tsukumijima.netのjson形式のAPIのURL
url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code

try:
    response = requests.get(url)
    # ステータスコード200番台以外は例外とする
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:{}".format(e))
else:
    # json形式で取得
    weather_json = response.json()

def weatherNotice():
    # 今日・明日のフラッグ
    today = 1
    # 現在時刻の取得
    time_hour = datetime.now().hour
    # 0時から9時までは今日の天気
    if time_hour >= 0 and time_hour < 9:
        # 今日の天気
        telop=weather_json['forecasts'][0]['telop']
        # 最低・最高気温
        # min_temp=weather_json['forecasts'][0]['temperature']['min']['celsius']
        # max_temp=weather_json['forecasts'][0]['temperature']['max']['celsius']
    else:
        # 明日の天気
        telop=weather_json['forecasts'][1]['telop']
        # 最低・最高気温
        # min_temp=weather_json['forecasts'][1]['temperature']['min']['celsius']
        # max_temp=weather_json['forecasts'][1]['temperature']['max']['celsius']
        today=0
    pygame.mixer.init() #初期化
    if today==1:
        day="today"
    else:
        day="tomorrow"
    pygame.mixer.music.load("weather_files/"+day+".mp3") #読み込み
    pygame.mixer.music.play(1) #再生
    time.sleep(1.2)
    pygame.mixer.music.stop() #終了
    if telop=="晴れ":
        telop="sunny"
    elif telop=="曇り":
        telop="cloudy"
    elif telop=="雨":
        telop="rainy"
    elif telop=="雪":
        telop="snowy"
    elif telop=="雷":
        telop="thunder"
    elif telop=="雨のち晴れ":
        telop="rainy_sunny"
    elif telop=="晴れのち雨":
        telop="sunny_rainy"
    elif telop=="曇のち晴":
        telop="cloudy_sunny"
    elif telop=="曇のち時々晴":
        telop="cloudy_sometimes_sunny"
    else :
        telop="error"
    pygame.mixer.music.load("weather_files/"+telop+".mp3") #読み込み
    pygame.mixer.music.play(1) #再生
    time.sleep(5)
    pygame.mixer.music.stop() #終了
    pygame.mixer.quit() #終了
    print(telop)