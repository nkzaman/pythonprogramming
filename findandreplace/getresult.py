#!/usr/bin/python

import os
import sys
import string
import re

information = open("information/replacingvalues.txt", 'r')
output = open("result/output.txt", 'w')
field = open("field/values.txt", 'r')

with open("test/input.txt", 'r') as myfile:
      inline = myfile.read()

informations  = []
fields = []
dictionary = {}
i = 0

for line in information:
    informations.append(line.splitlines())
    
for lines in field:
    fields.append(lines.split())
    i = i+1;

if (len(fields) != len(informations) ):
    print "replacing values and values have different numbers"
    exit();
else:
    for i in range(0, i):
        rightvalue = str(informations[i])
        rightvalue = rightvalue.strip('[]')
        rightvalue = rightvalue[1:-1]
    
        leftvalue = str(fields[i])
        leftvalue = leftvalue.strip('[]')
        leftvalue = leftvalue.strip("'")
        
        dictionary[leftvalue] = rightvalue

    robj = re.compile('|'.join(dictionary.keys()))
    result = robj.sub(lambda m: dictionary[m.group(0)], inline)


    output.write(result)
    information.close;
    output.close;
    field.close;
