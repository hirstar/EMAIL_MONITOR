#!/usr/bin/python

import os
import re

date =''
data =''
(time, IPAddress, Country) = 0,0,0

print("\t DATE\t TIME\t IP ADDRESS \t COUNTRY")
filein = open('mail.log', 'r')

for data in filein:
    date = filein.readline()
    date = re.match('^\w{3,4}', data)
    print(date.group())
 
