#!/usr/bin/python

import time
import os
import re
import sys

IPAddress = ''
CalNo = ''
data =''
date = ''
times = ''

print("\t DATE\t TIME\t\t IP ADDRESS \t Email-Addr \t COUNTRY")
filein = open('mail.log', 'r')

for data in filein:
    date = re.match('\w{3,4}\s\d{2}', data)
    times = re.search('\d{2}:\d{2}:\d{2}' , data)
    IPAddress = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' , data)
   
    if IPAddress == None :
        print('\t' + date.group() + '\t' + times.group() + '\t' + '****')
        continue

    print('\t' + date.group() + '\t' + times.group() + '\t' + IPAddress.group() )
    #time.sleep(1)
