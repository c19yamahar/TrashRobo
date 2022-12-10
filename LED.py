import RPi.GPIO as GPIO
import time
import sys

#ポート番号の定義
Led_red_pin = 22
Led_blue_pin = 23
Led_green_pin = 12

#GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led_red_pin, GPIO.OUT)
GPIO.setup(Led_blue_pin, GPIO.OUT)
GPIO.setup(Led_green_pin, GPIO.OUT)

def red(flag):
    if flag:
        GPIO.output(Led_red_pin, GPIO.HIGH)
    else:
        GPIO.output(Led_red_pin, GPIO.LOW)

def blue(flag):
    if flag:
        GPIO.output(Led_blue_pin, GPIO.HIGH)
    else:
        GPIO.output(Led_blue_pin, GPIO.LOW)

def green(flag):
    if flag:
        GPIO.output(Led_green_pin, GPIO.HIGH)
    else:
        GPIO.output(Led_green_pin, GPIO.LOW)