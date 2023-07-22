import dht
import config

class DHT22_Sensor:
    sensor = None
    
    def __init__(self, pin):
        if pin is None:
            print("[DHT22] No pin!")
        if config.PIN_DHT_22 is not None:
            self.sensor = dht.DHT22(pin)

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