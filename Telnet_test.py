#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      vvyas
#
# Created:     19/06/2013
# Copyright:   (c) vvyas 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import getpass
import sys
import telnetlib

##HOST = "localhost"
HOST = "10.207.50.100"
print "before telnet"
tn = telnetlib.Telnet(HOST)
print "after Telnet"
tn.read_until("login as: ")
tn.write("root\r")
##if password:
tn.read_until("Password: ")
tn.write("airvana\n")
print "after the password"
tn.write("ls\n")

#root@10.207.50.100's password:

print tn.read_all()

#def main():


#if __name__ == '__main__':
#    main()
##user = raw_input("Enter your remote account user name")
##password = getpass.getpass()
##print "Please wait..."
##tn = telnetlib.Telnet(HOST)
#tn.write("exit\n")
