import network
import socket
from time import sleep
from machine import Pin, Timer, ADC
import dht
import utime
import urequests
import ujson

ssid = 'Shire'
password = 'yeet'


led = Pin("LED", Pin.OUT)
def blink():
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)
    
def say_hello():
    blink()
    blink()
    blink()

def connect():
    print("Attempting")
    led.value(0)
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        blink()
        sleep(1)
    print(wlan.ifconfig())
    led.value(1)
    
def disconnect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    led.value(0)


def send_record(temp, hum, payload):
        response = urequests.post("http://192.168.50.214:2000/hives/piehive/records", headers = {'content-type': 'application/json'}, data=ujson.dumps({
            'temperature': temp,
            'humidity': hum,
            'payload': payload
        })).json()
        print(response) 

ADC_ConvertedValue = machine.ADC(0)
DIN = Pin(19,Pin.IN)
conversion_factor = 3.3 / (65535)
sensor = dht.DHT22(Pin(13))

say_hello()
while True:
    try:
        sleep(120)
        sensor.measure()
        print(f"Temperature : {sensor.temperature():.1f}°C")
        print(f"Humidite    : {sensor.humidity():.1f}%")
        AD_value = ADC_ConvertedValue.read_u16() * conversion_factor
        print("The current Gas AD value = ",AD_value ,"V")
        if(DIN.value() == 1) :
            print("Gas not leakage!")
        else :
            print("Gas leakage!")
        connect()
        send_record(sensor.temperature(), sensor.humidity(), "f u v2")
        disconnect()
    except OSError as e:
        print("Failed reception")
