#! /usr/bin/python3
#

# pw.py - An insecure password locker program.

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if (len (sys.argv) < 2):
   print ()
   print ("Usage: python pw.py [account] - copy account password")
   sys.exit ()

szAccount = sys.argv [1]

if (szAccount in PASSWORDS):
   print ("Found it")
   # szPassword = (PASSWORDS [szAccount])
   # print (szPassword)
   # pyperclip.copy (szPassword)
   pyperclip.copy (PASSWORDS [szAccount])
else:
   print ("Not there!")

try:
   pyperclip.copy (PASSWORDS [szAccount])
   print ()
   print ("Password stored in system clipboard, ready for pasting.")
except:
   print ()
   print ("Account specified ->" + szAccount + "<- does not have a stored password.")

