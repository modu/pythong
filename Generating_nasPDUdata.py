#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vvyas
#
# Created:     08/08/2013
# Copyright:   (c) vvyas 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#07417108391184000000008002e0e0001e0201d011d127178080211001000010810600000000830600000000000a003103e5c004
import pprint
def main():
    temp_1="0741710839118400000000"
    temp_3="02e0e0001e0201d011d127178080211001000010810600000000830600000000000a003103e5c004"
    temp_3="07417108391184000000104202e0e0001e0201d011d127178080211001000010810600000000830600000000000a003103e5c004"
    temp = []
    for i in range(32):
        varun = temp_1 + str(i).zfill(2) + temp_3
        temp.append(varun)
    for i,a in enumerate(temp):
        print '%s "%s"' % (i,a)

def changeFunction():
    temp_1="07417108391184000000"
    temp_2="02e0e0001e0201d011d127178080211001000010810600000000830600000000000a003103e5c004"
    temp = []
    for x in range(2,3):
        for i in range(0,10):
            for j in range(0,10):
                varun = temp_1 + str(x) + str(0) + str(j) +str(i) + temp_2
                temp.append(varun)

    for i, a in enumerate(temp):
        print '%s "%s"' % (i+197,a)

if __name__ == '__main__':
    #main()
    changeFunction()
