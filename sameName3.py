#! /usr/bin/python3
#

def spam ():
   global eggs
   eggs = 'spam'
   return

def bacon ():
   eggs = 'bacon'
   return

def ham ():
   print (eggs)
   return

eggs = 42
ham()
print (eggs)
spam()
print (eggs)

