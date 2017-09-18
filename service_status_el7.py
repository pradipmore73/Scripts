#!/usr/bin/python
#
#       AUTHOR     :    PRADIP MORE
#       PURPOSE    :    Check Service is Running or not if Not Then Show Critical Message

import os
import subprocess

def chk_name(service_name):
        FNULL = open(os.devnull,'w')
        services = subprocess.Popen(["systemctl -t service -a | awk '{print $1}' | grep -i .service"],stdout=subprocess.PIPE,shell=True)
        (out,err) = services.communicate()
        list = []
        for name in out:
                list.extend(name.split("."))
        return list

        if service_name in list:
                return True
        else:
                return False

def chk_status(service_name):
        FNULL = open(os.devnull,'w')
        ret_code = subprocess.call(["service",service_name,"status"],stdout=FNULL,stderr=subprocess.STDOUT)
        if ret_code == 0:
                print service_name,"is Alive(OK)",ret_code
        else:
                print "CRITICAL",service_name,"STOPPED !!",ret_code

while True:
        service = raw_input("Enetr Service Name to Check :")
        service_name = service.lower()

        if chk_name(service_name) :
                chk_status(service_name)
                break
        else:
                print "<-  Please Enter Correct Service Name  ->"
                continue
