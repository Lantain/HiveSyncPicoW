from time import sleep

from sensors.dht22 import DHT22_Sensor
from sensors.mq135 import MQ135_Sensor

import api
import led
import wnet

dht_sensor = DHT22_Sensor()
mq_sensor = MQ135_Sensor()

def main():
    dht_value = dht_sensor.values()
    mq_value = mq_sensor.values()
    
    payload = {
        'temperature': dht_value['temperature'],
        'humidity': dht_value['humidity'],
        'air_quality': mq_value['analog']
    }
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
