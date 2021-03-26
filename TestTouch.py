import busio
import digitalio
import board
import sys
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

def listen():
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    cs = digitalio.DigitalInOut(board.D6)
    mcp = MCP.MCP3008(spi, cs)
    chan = AnalogIn(mcp, MCP.P1)
    
    for _ in range(500):
        if(chan.voltage >= 1):
            return True
    return False