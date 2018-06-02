#! /usr/bin/python3
#

def printPicnic (itemsDict, leftWidth, rightWidth):
   print ('PICNIC ITEMS'.center (leftWidth + rightWidth, '-'))
   for k, v in itemsDict.items ():
      print (k.ljust (leftWidth, '.') + str (v).rjust (rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

keyLength = 0
valueLength = 0

print ()
printPicnic (picnicItems, 12, 5)

print ()
printPicnic (picnicItems, 20, 6)

for key, value in picnicItems.items ():
   if (len (key) > keyLength):
      keyLength = len (key)

   if (len (str (value)) > valueLength):
      valueLength = len (str (value))

print ()
printPicnic (picnicItems, (keyLength + 1), (valueLength + 1))

