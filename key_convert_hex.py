#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vvyas
#
# Created:     18/06/2013
# Copyright:   (c) vvyas 2013
# Licence:     Do what ever you want man. i am cool wit it :)
#-------------------------------------------------------------------------------

#key = [186,153,166,85,84,79,185,72,87,21,215,100,121,159,167,144]

def ConvertFromString():
    #keys = "186 153 166 85 84 79 185 72 87 21 215 100 121 159 167 144"
    keys  = "12 6 34 67 10 216 131 188 85 245 159 111 75 173 154 111"
    keys =  keys.split(" ")
    keys = map(int,keys)   #converting list from  ['186' , '153', .... ] to [ 186, 153, ..]
    #print keys
    count = 0
    temp = []
    for x in keys:
        temp.append(hex(int(x)))
        count = count +1
    print temp

def takeSingleInput():
    DecimalValue = input("Please input Decimal Value to be converted to Hex")
    print "Converted hex value is "
    print hex(DecimalValue)

def main():
    print "In the Main Function"
    takeSingleInput()
    #ConvertFromString()
if __name__ == '__main__':
    main()
