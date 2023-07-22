import framebuf
import time
from machine import SPI

class OLED_1inch3(framebuf.FrameBuffer):
    def __init__(self, pin_dc, pin_rst, pin_mosi, pin_sck, pin_cs, pin_key_a, pin_key_b):
        self.width = 128
        self.height = 64
        
        self.keyA = pin_key_a
        self.keyB = pin_key_b
        
        self.cs = pin_cs
        self.rst = pin_rst
        
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,2000_000)
        self.spi = SPI(1,20000_000,polarity=0, phase=0,sck=pin_sck,mosi=pin_mosi,miso=None)
        self.dc = pin_dc
        self.dc(1)
        self.buffer = bytearray(self.height * self.width // 8)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_HMSB)
        self.init_display()
        
        self.white =   0xffff
        self.balck =   0x0000
        
    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        """Initialize dispaly"""  
        self.rst(1)
        time.sleep(0.001)
        self.rst(0)
        time.sleep(0.01)
        self.rst(1)
        
        self.write_cmd(0xAE)#turn off OLED display

        self.write_cmd(0x00)   #set lower column address
        self.write_cmd(0x10)   #set higher column address 

        self.write_cmd(0xB0)   #set page address 
      
        self.write_cmd(0xdc)    #et display start line 
        self.write_cmd(0x00) 
        self.write_cmd(0x81)    #contract control 
        self.write_cmd(0x6f)    #128
        self.write_cmd(0x21)    # Set Memory addressing mode (0x20/0x21) #
    
        self.write_cmd(0xa0)    #set segment remap 
        self.write_cmd(0xc0)    #Com scan direction
        self.write_cmd(0xa4)   #Disable Entire Display On (0xA4/0xA5) 

        self.write_cmd(0xa6)    #normal / reverse
        self.write_cmd(0xa8)    #multiplex ratio 
        self.write_cmd(0x3f)    #duty = 1/64
  
        self.write_cmd(0xd3)    #set display offset 
        self.write_cmd(0x60)

        self.write_cmd(0xd5)    #set osc division 
        self.write_cmd(0x41)
    
        self.write_cmd(0xd9)    #set pre-charge period
        self.write_cmd(0x22)   

        self.write_cmd(0xdb)    #set vcomh 
        self.write_cmd(0x35)  
    
        self.write_cmd(0xad)    #set charge pump enable 
        self.write_cmd(0x8a)    #Set DC-DC enable (a=0:disable; a=1:enable)
        self.write_cmd(0XAF)
    def show(self):
        self.write_cmd(0xb0)
        for page in range(0,64):
            self.column = 63 - page              
            self.write_cmd(0x00 + (self.column & 0x0f))
            self.write_cmd(0x10 + (self.column >> 4))
            for num in range(0,16):
                self.write_data(self.buffer[page*16+num])

display = None

def init_display(pin_dc, pin_rst, pin_mosi, pin_sck, pin_cs):
    display = OLED_1inch3(pin_dc, pin_rst, pin_mosi, pin_sck, pin_cs)
    display.fill(0x0000) 
    display.show()
    display.rect(0,0,128,64,display.white)
    time.sleep(0.5)
    display.show()
    display.rect(10,22,20,20,display.white)
    time.sleep(0.5)
    display.show()
    display.fill_rect(40,22,20,20,display.white)
    time.sleep(0.5)
    display.show()
    display.rect(70,22,20,20,display.white)
    time.sleep(0.5)
    display.show()
    display.fill_rect(100,22,20,20,display.white)
    time.sleep(0.5)
    display.show()
    time.sleep(1)

def show_text(text):
    if display is None:
        print("[OLED1.3] Init display first")
        return
    
    display.fill(0x0000)
    display.text(text, 1,27, display.white)
    display.show()
    
        