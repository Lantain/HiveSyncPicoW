import config
from machine import Pin, Timer, ADC
conversion_factor = 3.3 / (65535)

class MQ135_Sensor:
    ADC_ConvertedValue = None
    DIN = None
    
    def __init__(self) -> None:
        if config.PIN_MQ135_ADC is not None:
            self.ADC_ConvertedValue = ADC(0)
        if config.PIN_MQ135_DIN is not None:
            self.DIN = Pin(19,Pin.IN)

    def values(self):
        if self.ADC_ConvertedValue is not None and self.DIN is not None:
            AD_value = self.ADC_ConvertedValue.read_u16() * conversion_factor
            DIN_value = self.DIN.value()
            
            return { 'air_quality': AD_value, 'air_quality_warn': DIN_value }
        
    def log(self):
        v = self.values()
        print("== MQ135: ==")
        print("The current Gas AD value = ",v["air_quality"],"V")
        print("The current DIN value: ",v["air_quality_warn"])