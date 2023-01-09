import RPi.GPIO as GPIO
import time
import sys

#ポート番号
Trig = 27
Echo = 18

#GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

#HC-SR04で距離を測定する関数
def read_distance():
    GPIO.output(Trig, GPIO.HIGH)            #GPIO27の出力をHigh(3.3V)にする
    time.sleep(0.00001)                     #10μ秒間待つ
    GPIO.output(Trig, GPIO.LOW)             #GPIO27の出力をLow(0V)にする

    while GPIO.input(Echo) == GPIO.LOW:     #GPIO18がLowの時間
        sig_off = time.time()
    while GPIO.input(Echo) == GPIO.HIGH:    #GPIO18がHighの時間
        sig_on = time.time()

    duration = sig_on-sig_off             #GPIO18がHighしている時間を算術
    distance = duration * 34000 / 2         #距離を求める(cm)
    return distance