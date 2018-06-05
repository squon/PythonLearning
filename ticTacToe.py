#! /usr/bin/python3
#

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard (board):
   print (board ['top-L'] + '|' + board ['top-M'] + '|' + board ['top-R'])
   print ('-+-+-')
   print (board ['mid-L'] + '|' + board ['mid-M'] + '|' + board ['mid-R'])
   print ('-+-+-')
   print (board ['low-L'] + '|' + board ['low-M'] + '|' + board ['low-R'])

def checkForWinner (board):
   #
   # Check for horizontal wins
   #
   if (board ['top-L'] == board ['top-M'] and board ['top-M'] == board ['top-R']) and (board ['top-L'] != ' '):
      return (board ['top-L'])
   if (board ['mid-L'] == board ['mid-M'] and board ['mid-M'] == board ['mid-R']) and (board ['mid-L'] != ' '):
      return (board ['mid-L'])
   if (board ['low-L'] == board ['low-M'] and board ['low-M'] == board ['low-R']) and (board ['low-L'] != ' '):
      return (board ['low-L'])

   #
   # Check for veritcal wins
   #
   if (board ['top-L'] == board ['mid-L'] and board ['mid-L'] == board ['low-L']) and (board ['top-L'] != ' '):
      return (board ['top-L'])
   if (board ['top-M'] == board ['mid-M'] and board ['mid-M'] == board ['low-M']) and (board ['top-M'] != ' '):
      return (board ['top-M'])
   if (board ['top-R'] == board ['mid-R'] and board ['mid-R'] == board ['low-R']) and (board ['top-R'] != ' '):
      return (board ['top-R'])

   #
   # Check for diagonal wins
   #
   if (board ['top-L'] == board ['mid-M'] and board ['mid-M'] == board ['low-R']) and (board ['top-L'] != ' '):
      return (board ['top-L'])
   if (board ['low-L'] == board ['mid-M'] and board ['mid-M'] == board ['top-R']) and (board ['low-L'] != ' '):
      return (board ['top-L'])

   return (False)

# print ()
# printBoard (theBoard)

# print ()
# printBoard (theBoard)
# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

turn = 'X'

for i in range (9):
   print ()
   printBoard (theBoard)

   move = ''

   while (True):
      print ()
      print ('Turn for ' + turn + '. Move on which space?  ', end='')

      move = input ()

      if (move not in theBoard):
         print ("You specified an illegal position")
         continue

      if (theBoard [move] != ' '):
         print ("The space specified has already been used")
         continue

      break

   theBoard [move] = turn

   winner = checkForWinner (theBoard)

   if (winner != False):
      break

   if turn == 'X':
      turn = 'O'
   else:
      turn = 'X'

if (winner != False):
   print ()
   print ("We have a winner:  " + winner)
   print ()
else:
   print ()
   print ("No winner!")

printBoard (theBoard)

