import config
import network
import modules.led as led
from time import sleep

wlan = network.WLAN(network.STA_IF)

def connect():
    print("Attempting")
    led.value(0)
    #Connect to WLAN
    wlan.active(True)
    wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        led.blink()
        sleep(1)
    print(wlan.ifconfig())
    led.value(1)
    
def disconnect():
    wlan.active(False)
    led.value(0)
