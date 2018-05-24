#! /usr/bin/python3
#

print ()
print ('----- Chapter One: -----')

print ()
print ('Mathematical operators:')
print ()
print ('** - exponent                          -  2 ** 3 = 8')
print ('%  - modulus/remainder                 - 22 %  8 = 6')
print ('// - integer division/floored quotient - 22 // 8 = 2')
print ('/  - division                          - 22 /  8 = 2.75')
print ('*  - multiplication                    -  3 *  5 = 15')
print ('-  - subtraction                       -  5 -  2 = 3')
print ('+  - addition                          -  2 +  2 = 4')

print ()
print ('Data types:')
print ()
print ('1.  Integers')
print ('2.  Floating-point numbers')
print ('3.  Strings')

print ()
print ('String concatenation:  +')
print ()
print ("Example:  'Alice' + ' in ' + 'Wonderland'")
print ("Result: ->" + 'Alice' + ' in ' + 'Wonderland' + "<-")

print ()
print ('String replication:  *')
print ()
print ("Example:  'Alice ' * 5")
print ("Result: ->" + 'Alice ' * 5 + "<-")

print ()
print ('Variable names:')
print ()
print ('1.  It can only be one word.')
print ('2.  It can use only letters, numbers, and the underscore (_) character.')
print ("3.  It can't begin with a number")

print ()
print ('Functions introduced:')
print ()
print ('print ()')
print ('input ()')
print ('len ()')
print ('str ()')
print ('int ()')
print ('float ()')

print ()
print ('----- Chapter Two: -----')

print ()
print ('Comparison operators:')
print ()
print ('== - Equal to')
print ('!= - Not equal to')
print ('<  - Less than')
print ('>  - Greater than')
print ('<= - Less than or equal to')
print ('>= - Greater than or equal to')

print ()
print ('Boolean operators:')
print ()
print ('1.  not')
print ('2.  and')
print ('3.  or')

print ()
print ('Flow control statements:')
print ()
print ('if, elif, else')
print ()
print ('Example:')
print ('if name == yourname:')
print ('   print (yourname)')
print ('elif age == yourage:')
print ('   print (yourage)')
print ('else:')
print ("   print ('Something else')")

print ()
print ('while')
print ()
print ('Example:')
print ('while number < 5:')
print ('   print (number)')
print ('   number = number + 1')

print ()
print ('break, continue')
print ()
print ('Example:')
print ('while number < 5:')
print ('   print (number)')
print ('   number = number + 1')
print ('   if (number > 3):')
print ('      break')
print ('   else:')
print ('      continue')

print ()
print ('Truthy and falsey:')
print ("0, 0.0, and '' (the empty string) are considered False")
print ()
print ('Example:')
print ("name = ''")
print ('while not name:')
print ("   print ('Enter your name:  ')")
print ('   name = input ()')

print ()
print ('for loops and ranges')
print ()
print ('Example:')
print ("print 'My name is")
print ('for i in range (5):')
print ("   print ('Jimmy Five Times (' + str (i) + ')')")
print ()
print ('Output:')

for i in range (5):
   print ('Jimmy Five Times (' + str (i) + ')')

print ()
print ('starting, stopping, and stepping arguments to range ()')
print ()
print ('Example:')
print ('for i in range (0, 10, 2):')
print ('   print (i)')
print ()
print ('Output:')

for i in range (0, 10, 2):
   print (i)

print ()
print ('Importing modules:')
print ('1. import <module>')
print ('2. import <module>, <module>')
print ('3. from <module> import *')
print ()
print ('Example:')
print ('import random')
print ('import os')
print ('import sys, math')
print ('for i in range (5):')
print ('   print (random.randint (1,10))')

print ()
print ('Sample output:')

import os
import random, sys
from math import *
# from sys, math import *
for i in range (5):
   print (random.randint (1,10))

print ()
print ('Example:')
print ('import sys')
print ('while True:')
print ("   print ('Type exit to exit.')")
print ('   response = input ()')
print ("   if response == 'exit':")
print ('      sys.exit ()')
print ("   print ('You typed ' + response + '.')")

def Test_SysExit ():
   import sys
   while True:
      print ('Type exit to exit.')
      response = input ()
      if response == 'exit':
         sys.exit ()
      print ('You typed ' + response + '.')

print ()
print ('Functions introduced:')
print ()
print ('range (<start>, <stop>, <step>) - first parameter is inclusive, second parameter is excluvie')
print ('random.randint (<start>, <stop>) - passed in parameters are inclusive')
print ('sys.exit ()')
print ('round ()')
print ('abs ()')

print ()
print ('----- Chapter Three: -----')

print ()
print ('Create your own Functions:')

print ()
print ('def <function name> ():')
print ()
print ('Example:')

print ('def hello ():')
print ("   print ('Howdy!')")
print ('hello ()')
print ('hello ()')

print ()
print ('Output:')

def hello ():
   print ('Howdy!')
hello ()
hello ()

print ()
print ('def <function name> (<variable name>):')
print ()
print ('Example:')

print ('def hello (name):')
print ("   print ('Hello ' + name)")
print ("hello ('Alice')")
print ("hello ('Bob')")

def hello (name):
   print ('Hello ' + name)
hello ('Alice')
hello ('Bob')

print ()
print ('Function cannot be overloaded - function is simply redefined:')

def testOverload ():
   hello ('cutie')
   hello ()

print ()
print ('Return values and return statements:')

print ()
print ('Example:')
print ('return')
print ('return <value or expression>')

print ()
print ('None value (NoneType):')

print ()
print ('Example:')

print ("spam = print ('Hello!')")
print ('if (None == spam):')
print ("   print ('True')")
print ('else:')
print ("   print ('False')")

print ()
print ('Output:')
spam = print ('Hello!')
if (None == spam):
   print ('True')
else:
   print ('False')

print ()
print ('Keyword Arguements and print ():')

print ()
print ('Example:')
print ("print ('Hello', end='')")
print ("print ('World')")

print ()
print ('Output:')
print ('Hello', end='')
print ('World')

print ()
print ('Example:')
print ("print ('cats', 'dogs', 'mice', sep=', ')")

print ()
print ('Output:')
print ('cats', 'dogs', 'mice', sep=', ')

print ()
print ('global statement:')

print ()
print ('Example:')

print ('def spam ():')
print ('   global eggs')
print ("   eggs = 'spam'")
print ('   return')

print ("eggs = 'global'")
print ('print (eggs)')
print ('spam ()')
print ('print (eggs)')

print ()
print ('Output:')

def spam ():
   global eggs
   eggs = 'spam'
   return

eggs = 'global'
print (eggs)
spam ()
print (eggs)

print ()
print ('Exception handling:')

print ('try, except')

