#! /usr/bin/python3
#

def addBullet (someList):
   newList = []

   for szLine in (someList):
      newList.append (("* " + szLine))

   return (newList)

import pyperclip

szClipboard = pyperclip.paste ()

listLinesOfText = szClipboard.split ('\n')

newList = addBullet (listLinesOfText)

szNewClipboard = '\n'.join (newList)

pyperclip.copy (szNewClipboard)

