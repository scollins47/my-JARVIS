import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

f = open("data.txt", "a")

#create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#create the chip select (CS with a bar)
cs = digitalio.DigitalInOut(board.D5)

#create the mcp object
mcp = MCP.MCP3008(spi, cs)

#create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
print("ADC raw value:", chan.value)
print("Starting While Loop")
prevVal = chan.value
prevVol = chan.voltage
count = 0
while True:
    valu = chan.value
    volt = chan.voltage
    to_write = str(valu) + ", " + str(volt) + "V, " + str(count)
    if(abs(prevVal - valu) < 1900): #if the voltage is +-.5 from previous
        count+= 1 #add 1 to count
        if(count > 2750 and volt >= 2): #if its mostly just 1 value print it and reset count
            f.write(to_write + '\n')
            print('motion detected')
            count = 0
            continue
        elif count > 2750:
            f.write(to_write + '\n')
            count = 0
            continue
    else:
        f.write(to_write + '\n')
        count = 0
        prevVal = valu
        prevVol = volt
f.write('\n')
f.close()

