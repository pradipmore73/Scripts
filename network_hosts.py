#!/usr/bin/python
##########################################################################
###   AUTHOR  : PRADIP MORE                                            ###
###   PURPOSE : Status of Hosts in a Subnet Network are Active or Dead ###
###   Python Version : Python 2.7.5                                    ###  
##########################################################################

import os
import subprocess
cidr = {'32' : 1 , '31' : 2 , '30' : 4 , '29' : 8 , '28' : 16 , '27' : 32 , '26' : 64 , '25' : 128}
mt = 0
while True:
        ip_address = raw_input("Enter IP Address : ")
        octets = map(int, ip_address.split('/')[0].split('.')) # '1.2.3.4'=>[1, 2, 3, 4]

        if (len(octets) == 4) and (int(octets[0] >= 1) <= 223) and (int(octets[0]) != 127) and (int(octets[0]) != 169 or int(octets[1]) != 254) and (0 <= int(octets[1]) <= 255 and 0 <= int(octets[2]) <= 255 and 0 <= int(octets[3]) <= 255):

                if "/" in ip_address:
                        mt = (ip_address.split('/')[1])
                        if (int(mt) >= 25 and int(mt) <=32):
                                break
                        else:
                                print "\n Entered CIDR is INVALID"
                                continue

                else:
                        mt = raw_input("Enter CIDR : "+ip_address+"/")
                        if (int(mt) >= 25 and int(mt) <=32):
                                break
                        else:
                                print "\n Entered CIDR is INVALID"
                                continue
                break

        else:
                print "\nThe IP address is INVALID! Please retry!\n"
                continue

def ping_ip(ip,rang):
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    mask = []
    for i in range(0,32):
                if i <= int(rang) :
                        mask.append("1")
                        continue
                else:
                        mask.append("0")
                        continue

    str1 = ''.join(str(e) for e in mask)
    print str1,": Mask"
    print binary.zfill(32),": ip"
    print "================================"
    network = []
    ip_bin_list = list(binary.zfill(32))

    for i in range(len(mask)):
                if str1[i] == "1" and ip_bin_list[i] == "1":
                        network.append("1")
                else:
                        network.append("0")

    str2 = ''.join(str(f) for f in network)
    print str2,": Network Address"
    network_decimal = []
    a1 = [] ; a2 = [] ; a3 = [] ; a4 = []
    for i in range(len(str2)):
                if i <= 7 :
                        a1.append(str2[i])
                elif i >= 8 and i <= 15:
                        a2.append(str2[i])
                elif i >= 16 and i <= 23:
                        a3.append(str2[i])
                elif i >= 24 and i <= 32:
                        a4.append(str2[i])

    b1 = ''.join(a1); b2 = ''.join(a2) ; b3 = ''.join(a3) ; b4 = ''.join(a4)

    result = []
    result.append(int(b1,2))
    result.append(int(b2,2))
    result.append(int(b3,2))
    result.append(int(b4,2))

    print "----------------------------"
    print "HOSTS                 STATUS"
    print "----------------------------"
    FNULL = open(os.devnull,'w')
    for hosts in range(int(b4,2),cidr[mt]+int(b4,2)):
        response = subprocess.call(["ping","-c", "1", "-w", "1",str(result[0])+"."+str(result[1])+"."+str(result[2])+"."+str(hosts)],stdout=FNULL,stderr=subprocess.STDOUT)
        if response == 0:
                print str(result[0])+"."+str(result[1])+"."+str(result[2])+"."+str(hosts), " Active"
        else:
                print str(result[0])+"."+str(result[1])+"."+str(result[2])+"."+str(hosts), " Dead"
ping_ip(octets,mt)
