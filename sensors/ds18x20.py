import config
import onewire, ds18x20, time

class DS18X20_Sensor:
    sensor = None
    roms = None
    def __init__(self, pin):
        if pin is None:
            print("[DS18X20] No pin!")
            
        if config.PIN_DHT_22 is not None:
            self.sensor = ds18x20.DS18X20(onewire.OneWire(pin))
            self.roms = self.sensor.scan()
    
    def values(self):
        if self.sensor is not None:
            self.sensor.convert_temp()
            time.sleep_ms(800)
            deg = None
            for rom in self.roms:
              deg = self.sensor.read_temp(rom)
            
            return {
                'temperature_ds': deg
            }
    
    def log(self):
        v = self.values()
        print("== DS18X20: ==")
        print(f"Temperature : {v['temperature_ds']:.1f}°C")