#!/usr/bin/python

#########################################################
#       PURPOSE : Find Common Factor in two Numbers     #
#       AUTHOR  : PRADIP MORE                           #
#########################################################

a = int(input("Enter 1st Number  :"))
b = int(input("Enter 2nd Number  :"))
list1 = []
list2 = []
list = []
for i in range(1,100):
    if((a%i)==0):
        list1.append(i)

for j in range(1,100):
    if ((b%j)==0):
        list2.append(j)

print "List 1 : ",list1
print "List 2 : ",list2

for item in range(1,len(list1)):
        for i in range(1,len(list2)):
                if(list1[item] == list2[i]) :
                        list.append(list1[item])

print "Comman Factors are : ",list
