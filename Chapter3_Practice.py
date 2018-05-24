#! /usr/bin/python3
#

def collatz (nNumber):
   if (nNumber % 2 == 0):
      nResult = nNumber // 2
   else:
      nResult = 3 * nNumber + 1

   print (nResult)
   return (nResult)

fSuccess = False

print ()
while (fSuccess == False):
   try:
      szResponse = input ( 'Enter an integer:  ')
      nNumeric = int (szResponse)
      fSuccess = True
   except:
      print ()
      print ('You enter: ->' + str(szResponse) + '<-.  That is not an integer.')

nResult = nNumeric
while (nResult != 1):
   nResult = collatz (nResult)
