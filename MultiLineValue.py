#! /usr/bin/python3
#

dictMyDict = {'_SomeKey_': "sg-0e8b0c7f\", \n\"sg-c29116b3"}

print ()
print (dictMyDict)

print ()
print ("Line one\nLinetwo")

szLine1 = "Line one"
szLine2 = "Line two"

szCombined = szLine1 + "\n" + szLine2

print ()
print (szCombined)

szSG1 = "sg-0e8b0c7f"
szSG2 = "sg-c29116b3"

szSGValue = szSG1 + '",' + "\n" + '"' + szSG2

print ()
print (szSGValue)

listSGValues = [ szSG1, szSG2 ]
print ()
print (listSGValues)

szSGJoinValue = ("\",\n\"").join (listSGValues)

print ()
print (szSGJoinValue)
