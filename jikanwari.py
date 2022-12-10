import pygame.mixer
import time

# 時間割を読み上げる関数
def jikanwariSpeech(day):
    if day<7:
        # 土、日、月曜日の場合は月曜日の時間割を読み上げる
        if day == 0 or day == 6 or day == 1:
            day = "monday"
        elif day == 2:
            day = "tuesday"
        elif day == 3:
            day = "wednesday"
        elif day == 4:
            day = "thursday"
        elif day == 5:
            day = "friday"
        pygame.mixer.init() #初期化
        pygame.mixer.music.load("jikanwari_files/"+day+".mp3") #読み込み
        pygame.mixer.music.play(1) #再生
        time.sleep(15)
        pygame.mixer.music.stop() #終了
    else:
        print("error")