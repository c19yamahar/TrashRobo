import RPi.GPIO as GPIO
import time

# モータのピン番号定義
motorRight1=22
motorRight2=23
motorLeft1=24
motorLeft2=25

# GPIO setting
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorRight1, GPIO.OUT)
GPIO.setup(motorRight2, GPIO.OUT)
GPIO.setup(motorLeft1, GPIO.OUT)
GPIO.setup(motorLeft2, GPIO.OUT)

# 前進
def goAlong():
    GPIO.output(motorRight1, GPIO.HIGH)
    GPIO.output(motorRight2, GPIO.LOW)
    GPIO.output(motorLeft1, GPIO.HIGH)
    GPIO.output(motorLeft2, GPIO.LOW)
    time.sleep(0.2)

# 後進
def back():
    GPIO.output(motorRight2, GPIO.HIGH)
    GPIO.output(motorRight1, GPIO.LOW)
    GPIO.output(motorLeft2, GPIO.HIGH)
    GPIO.output(motorLeft1, GPIO.LOW)
    time.sleep(0.2)

# 停止
def stop():
    GPIO.output(motorRight1, GPIO.LOW)
    GPIO.output(motorRight2, GPIO.LOW)
    GPIO.output(motorLeft1, GPIO.LOW)
    GPIO.output(motorLeft2, GPIO.LOW)
    time.sleep(0.2)