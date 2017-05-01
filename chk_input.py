#!/usr/bin/python

#########################################################
#                                                       #
#       Author  : PRADIP MORE                           #
#       Purpose : To Check input is Aplphabet/Number    #
#                                                       #
#########################################################


input = raw_input("Enter Something : ")         # take row input from user

if input.isalpha() :                            # check if it is Aplphabet
        print input+" is Alphabet"

elif input.isdigit() :                          # if not Alphabet then check for a Digit
        print input+" is Digit"

elif input.isalnum() :                          # Check for Combination of Alphabet and Numbers
        print input+" is Alphanumeric String"
