#!/usr/bin/python

#########################################################################
##      AUTHOR  : PRADIP MORE                                           #
##      PURPOSE : Python Script to Generate Random Password             #
##               (Minimun 1 upper,1 lower,1 special,1 digit)            #
#########################################################################
import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
digit = "0123456789"
special = "!@#$%^&*()"
len = 0

upper = list(upper)                     # make List
lower = list(lower)
digit = list(digit)
special = list(special)

try :

        len = int(input("Enter Length of Passwd (min 8 char) :"))

        if (len < 8):
                len = 8
                print "Using Default (8 Characters)"
except SyntaxError:
        len = 8
        print "Using Default (8 Characters)"


def passwd_gen(length):

        u = random.randint(1,length-3)
        l = random.randint(1,length-2-u)
        c = random.randint(1,length-1-u-l)
        n = length-u-l-c

        passwd = random.sample(upper,u)+random.sample(lower,l)+random.sample(special,c)+random.sample(digit,n)

        random.shuffle(passwd)
        return "".join(passwd)

your_passwd = passwd_gen(len)
print your_passwd
