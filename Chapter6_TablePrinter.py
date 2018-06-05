#! /usr/bin/python3
#

fDebug=0

headerData = ['fruits', 'names', 'animals']

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable (tableData, headerData):
   #
   # Confirm header columns match data columns
   #
   if (len (headerData) != len (tableData)):
      print ()
      print ("Header data doesn't match column count")

      return 1

   columnWidths = [0] * len (tableData)

   #
   # Determine the required column width
   #
   for counter in range (0, len (headerData)):
      columnWidths [counter] = len (headerData [counter])

   nColumn = 0
   for innerList in tableData:
      for element in innerList:
         elementWidth = len (element)

         if (elementWidth > columnWidths [nColumn]):
            columnWidths [nColumn] = elementWidth

      nColumn += 1

   nColumn = 0
   szLine = ''
   for header in headerData:
      szLine += header.rjust (columnWidths [nColumn]) + ' '
      nColumn += 1

   print ()
   if (fDebug == 0):
      print (szLine.rstrip ())
   else:
      print ("->" + szLine.rstrip () + "<-")

   szLine = ''
   for width in columnWidths:
      szLine += "-" * width + ' '

   if (fDebug == 0):
      print (szLine.rstrip ())
   else:
      print ("->" + szLine.rstrip () + "<-")

   rowCount = len (tableData [0])
   columnCount = len (tableData)

   for column in range (0, rowCount):
      szLine = ''
      for row in range (0, columnCount):
         szLine += tableData [row][column].rjust (columnWidths [row]) + ' '

      if (fDebug == 0):
         print (szLine.rstrip ())
      else:
         print ("->" + szLine.rstrip () + "<-")

   return 0

nReturn = printTable (tableData, headerData)

if (nReturn != 0):
   print ()
   print ("Error trying to print table")

