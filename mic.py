import speech_recognition as sr 
# 音声入力 
def speechInput():
    while True: 
        r = sr.Recognizer() 
        with sr.Microphone() as source: 
            print("音声認識開始") 
            audio = r.listen(source) 
        try: 
            # Google Web Speech APIで音声認識 
            text = r.recognize_google(audio, language="ja-JP") 
        except sr.UnknownValueError: 
            print("音声認識失敗")
        except sr.RequestError as e: 
            print("API通信失敗" " {0}".format(e))
        else: 
            print(text)
            return text