from time import sleep

from sensors.dht22 import DHT22_Sensor
from sensors.mq135 import MQ135_Sensor
from sensors.model import build_sensors_payload
from machine import Pin, ADC

import api
import config
import modules.led as led
import modules.wnet as wnet
# import modules.oled1_3 as oled
sensors = list([
    DHT22_Sensor(
        Pin(config.PIN_DHT_22)
    ),
    MQ135_Sensor(
        ADC(config.PIN_MQ135_ADC), 
        Pin(config.PIN_MQ135_DIN, Pin.IN)
    )
])

def mainstep():
    payload = build_sensors_payload(sensors)
    
    wnet.connect()
    api.send_record(payload)
    wnet.disconnect()

if __name__ == '__main__':
    led.say_hello()
    # if config.OLED13_ENABLED:
    #     oled.init_display(
    #         Pin(config.PIN_OLED13_DC, Pin.OUT),
    #         Pin(config.PIN_OLED13_RST, Pin.OUT),
    #         Pin(config.PIN_OLED13_MOSI),
    #         Pin(config.PIN_OLED13_SCK),
    #         Pin(config.PIN_OLED13_CS, Pin.OUT),
    #         Pin(config.PIN_OLED13_KEY_A, Pin.IN, Pin.PULL_UP),
    #         Pin(config.PIN_OLED13_KEY_B, Pin.IN, Pin.PULL_UP)
    #     )
        
    while True:
        try:
            sleep(config.STEP_SLEEP)
            mainstep()
        except OSError as e:
            print("Failed reception")
            led.panic()
