import time
import datetime

import motorControll
import mic
import weather_forecast
import jikanwari
import distance


while True:
    mic_id=mic.speechInput()
    if "こっち来て" in mic_id or "おいで" in mic_id:
        mic_id = 1
    elif "時間割" in mic_id or "日課" in mic_id :
        mic_id = 2
    elif "天気" in mic_id :
        mic_id = 3

    #ゴミ箱移動(接近)
    if mic_id == 1:
        time.sleep(0.5)
        motorControll.goAlong()
        time_bg=time.time()
        while True:
            cm = distance.read_distance()
            print("distance=", int(cm), "cm")
            if cm<10:
                break
        time_en=time.time()
        # 来るまでの時間を計測
        dis_time=time_en-time_bg
        motorControll.stop()
        time.sleep(10)
        motorControll.back()
        time.sleep(dis_time)
        motorControll.stop()
    
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