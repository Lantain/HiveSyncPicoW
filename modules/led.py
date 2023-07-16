from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)
led.value(0)

def blink():
    led.value(0)
    sleep(1)
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)
    
def say_hello():
    blink()
    blink()
    blink()
    
def panic():
    print("PANIC")
    for i in range(10):
        blink()
    
def value(v):
    led.value(v)