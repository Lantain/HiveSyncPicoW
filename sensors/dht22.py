import dht
import config
from machine import Pin

class DHT22_Sensor:
    sensor = None
    
    def __init__(self):
        if config.PIN_DHT_22 is not None:
            self.sensor = dht.DHT22(Pin(13))

    def values(self):
        if self.sensor is not None:
            self.sensor.measure()
            return {
                'temperature': self.sensor.temperature(),
                'humidity': self.sensor.humidity()
            }
            
    def log(self):
        v = self.values()
        print("== DHT22: ==")
        print(f"Temperature : {v['temperature']:.1f}°C")
        print(f"Humidity    : {v['humidity']:.1f}%")