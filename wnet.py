import config
import wnet
import led
from time import sleep

def connect():
    print("Attempting")
    led.value(0)
    #Connect to WLAN
    wlan = wnet.WLAN(wnet.STA_IF)
    wlan.active(True)
    wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        led.blink()
        sleep(1)
    print(wlan.ifconfig())
    led.value(1)
    
def disconnect():
    wlan = wnet.WLAN(wnet.STA_IF)
    wlan.active(False)
    led.value(0)
