#! /usr/bin/python3
#

def ListToSentence (listOfData):
   nListLength = len (listOfData)
   if (nListLength > 2):
      for element in (listOfData [0:-1]):
         print (element + ", ", end='')
         continue
      print ('and ' + listOfData [len (listOfData) - 1])
   elif (nListLength == 2):
      print (listOfData [0] + ' and ' + listOfData [1])
   elif (nListLength == 1):
      print (listOfData [0])
   else:
      print ("You didn't enter any data")

print ("Give me a list of data.  Empty <Enter> when you're done with the list.")

listInput = []
dataElement = input ()

while (dataElement != ''):
   listInput.append (dataElement)
   dataElement = input ()

ListToSentence (listInput)

def EffectiveComment ():
   print (listInput)
   print (listInput [0:-1])

   for element in listInput [0:-2]:
      print (element + ", ", end='')
      continue

   print ('and ' + listInput [len (listInput) - 1])

