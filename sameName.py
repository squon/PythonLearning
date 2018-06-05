#! /usr/bin/python3
#

def spam ():
   eggs = 'spam local'
   print (eggs)
   return

def bacon ():
   eggs = 'bacon local'
   print (eggs)
   spam ()
   print (eggs)
   return

eggs = 'global'
bacon ()
print (eggs)

