import dht
import config
from machine import Pin

class DHT22_Sensor:
    sensor: dht.DHT22 = None
    
    def __init__(self) -> None:
        if config.PIN_DHT_22 is not None:
            self.sensor = dht.DHT22(Pin(13))

    def values(self):
        if self.sensor is not None:
            self.sensor.measure()
            return {
                'temperature': self.sensor.temperature(),
                'humidity': self.sensor.humidity()
            }