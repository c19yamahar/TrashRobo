from collections import deque
from time import sleep
import numpy as np
import mediapipe as mp
import tensorflow as tf
import time
import datetime

import motorControll
import mic
import weather_forecast
import jikanwari
import LED


while True:
    LED.red(False)
    LED.green(True)
    mic_id=mic.speechInput()
    LED.green(False)
    LED.red(True)
    if "こっち来て" in mic_id or "おいで" in mic_id:
        mic_id = 1
    elif "時間割" in mic_id or "日課" in mic_id :
        mic_id = 2
    elif "天気" in mic_id :
        mic_id = 3

    #ゴミ箱移動(接近)
    if mic_id == 1:
        time.sleep(0.5)
        motorControll.motor_control(goAlong)
    
    # 時間割
    elif mic_id == 2:
        # 曜日の取得
        Day=datetime.datetime.now().weekday()
        # 8時前だったら当日, 8時以降だったら翌日
        now_hour=datetime.datetime.now().hour
        if now_hour>=8:
            Day+=1
        jikanwari.jikanwariSpeech(Day)

    # 天気予報
    elif mic_id == 3:
        weather_inf=weather_forecast.weatherNotice()
        print(weather_inf)