#!/usr/bin/python3
# Read data from AMS-IAQ-Core C

import pigpio

I2C_BUS = 1
IAQ_ADDR = 0x5a

def readAllBytes():
    try:
        pi = pigpio.pi()
        h = pi.i2c_open(I2C_BUS, IAQ_ADDR)
    except:
        print("Kann IAQ nicht oeffnen!")
    (c, b) = pi.i2c_read_device(h, 9)
    
    pi.i2c_close(h)
    # print(b)
    return b

def getValues(b):
    values = {}
    values["predict"] = b[0] << 8 | b[1]
    values["status"] = b[2]
    values["resistance"] = b[3] & 0x00 | b[4] << 16 | b[5] << 8 | b[6]
    values["tvoc"] = b[7] << 8 | b[8]
    return values

if __name__ == "__main__":
    rawdata = readAllBytes();
    for i in range(0, 9):
        print(rawdata[i])
    
    params = getValues(rawdata)
    print("predict = ", params["predict"])
    print("status = ", params["status"])
    print("resistance = ", params["resistance"])
    print("tvoc = ", params["tvoc"])





