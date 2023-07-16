from time import sleep

from sensors.dht22 import DHT22_Sensor
from sensors.mq135 import MQ135_Sensor
from sensors.model import build_sensors_payload
import api
import modules.led as led
import modules.wnet as wnet

sensors = list([
    DHT22_Sensor(),
    MQ135_Sensor()
])

def main():
    payload = build_sensors_payload(sensors)
    
    wnet.connect()
    api.send_record(payload)
    wnet.disconnect()


led.say_hello()
while True:
    try:
        sleep(120)
        main()                   
    except OSError as e:
        print("Failed reception")
        led.panic()
