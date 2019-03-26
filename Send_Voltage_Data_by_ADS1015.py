#!/usr/bin/env python
#coding: utf-8
import time, signal, sys
import math
from Adafruit_ADS1x15 import ADS1x15
import ambient

ADS1015 = 0x00
gain = 2
sps = 3300
roop = 150

adc = ADS1x15(ic=ADS1015)

ambi = ambient.Ambient(ID, "writeKey")

vol0 = 0
vol1 = 0
vol2 = 0
vol3 = 0

for num in range(roop):
        tmp0 = adc.readADCSingleEnded(0, gain, sps) * 30
        tmp1 = adc.readADCSingleEnded(1, gain, sps) * 30
        tmp2 = adc.readADCSingleEnded(2, gain, sps) * 30
        tmp3 = adc.readADCSingleEnded(3, gain, sps) * 30

        vol0 += math.pow(tmp0, 2)
        vol1 += math.pow(tmp1, 2)
        vol2 += math.pow(tmp2, 2)
        vol3 += math.pow(tmp3, 2)
        time.sleep(2)

out0 = math.sqrt(vol0/math.pow(roop,2))
out1 = math.sqrt(vol1/math.pow(roop,2))
out2 = math.sqrt(vol2/math.pow(roop,2))
out3 = math.sqrt(vol3/math.pow(roop,2))
#print out1
r = ambi.send({"d1": out0, "d2": out1, "d3": out2,  "d4": out3})
r.close()