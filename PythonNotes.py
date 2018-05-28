#! /usr/bin/python3
#

print ()
print ('----- Chapter One:  Programming Basics -----')

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
print ('----- Chapter Two:  Flow Control -----')

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
print ('if, elif, else')

print ()
print ('Example:')
print ()

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
print ()

print ('while number < 5:')
print ('   print (number)')
print ('   number = number + 1')

print ()
print ('break, continue')
print ()
print ('Example:')
print ()

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
print ()

print ("name = ''")
print ('while not name:')
print ("   print ('Enter your name:  ')")
print ('   name = input ()')

print ()
print ('for loops and ranges')
print ()
print ('Example:')
print ()

print ("print 'My name is")
print ('for i in range (5):')
print ("   print ('Jimmy Five Times (' + str (i) + ')')")
print ()
print ('Output:')
print ()

for i in range (5):
   print ('Jimmy Five Times (' + str (i) + ')')

print ()
print ('starting, stopping, and stepping arguments to range ()')
print ()
print ('Example:')
print ()

print ('for i in range (0, 10, 2):')
print ('   print (i)')
print ()
print ('Output:')
print ()

for i in range (0, 10, 2):
   print (i)

print ()
print ('Importing modules:')
print ('1. import <module>')
print ('2. import <module>, <module>')
print ('3. from <module> import *')
print ()
print ('Example:')
print ()

print ('import random')
print ('import os')
print ('import sys, math')
print ('for i in range (5):')
print ('   print (random.randint (1,10))')

print ()
print ('"Sample" output:')

import os
import random, sys
from math import *
# from sys, math import *
for i in range (5):
   print (random.randint (1,10))

print ()
print ('Example:')
print ()

print ('import sys')
print ('while True:')
print ("   print ('Type exit to exit.')")
print ('   response = input ()')
print ("   if response == 'exit':")
print ('      sys.exit ()')
print ("   print ('You typed ' + response + '.')")

print ()
print ("Output:")
print ()

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
print ('----- Chapter Three:  Functions -----')

print ()
print ('Create your own Functions:')

print ()
print ('def <function name> ():')
print ()
print ('Example:')
print ()

print ('def hello ():')
print ("   print ('Howdy!')")
print ('hello ()')
print ('hello ()')

print ()
print ('Output:')
print ()

def hello ():
   print ('Howdy!')
hello ()
hello ()

print ()
print ('def <function name> (<variable name>):')
print ()
print ('Example:')
print ()

print ('def hello (name):')
print ("   print ('Hello ' + name)")
print ("hello ('Alice')")
print ("hello ('Bob')")

print ()
print ('Output:')
print ()

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
print ()

print ('return')
print ('return <value or expression>')

print ()
print ('None value (NoneType):')

print ()
print ('Example:')
print ()

print ("spam = print ('Hello!')")
print ('if (None == spam):')
print ("   print ('True')")
print ('else:')
print ("   print ('False')")

print ()
print ('Output:')
print ()

spam = print ('Hello!')
if (None == spam):
   print ('True')
else:
   print ('False')

print ()
print ('Keyword Arguements and print ():')

print ()
print ('Example:')
print ()

print ("print ('Hello', end='')")
print ("print ('World')")

print ()
print ('Output:')
print ()
print ('Hello', end='')
print ('World')

print ()
print ('Example:')
print ()

print ("print ('cats', 'dogs', 'mice', sep=', ')")

print ()
print ('Output:')
print ()
print ('cats', 'dogs', 'mice', sep=', ')

print ()
print ('global statement:')

print ()
print ('Example:')
print ()

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
print ()

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

print ()
print ('----- Chapter Four:  Lists -----')

print ()
print ('Example 1-D lists:')
print ()

print ('[1, 2, 3]')
print ("['cat', 'bat', 'rat', 'elephant']")
print ("[100, 2.2, 'rat'] - mixed types okay")

print ()
print ("[] - empty list like ''")

print ()
print ("Negative indexes start from right side")

print ()
print ("Example:")
print ()

print ("spam = ['cat', 'bat', 'rat', 'elephant']")
print ('print (spam [-1])')

print ()
print ('Output:')
print ()

spam = ['cat', 'bat', 'rat', 'elephant']
print (spam [-1])

print ()
print ('Lists can contain lists:')

print ()
print ('Example 2-D lists:')
print ()

print ("spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]")
print ('print (spam [0])')
print ('print (spam [0][1])')
print ('print (spam [1][4])')

print ()
print ('Output:')
print ()

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print (spam [0])
print (spam [0][1])
print (spam [1][4])

print ()
print ('Sublists with slices:')
print ()
print ('Example:')
print ()
print ("spam = ['cat', 'bat', 'rat', 'elephant']")
print ('print (spam [0:4])')
print ('print (spam [1:3])')
print ('print (spam [0:-1])')
print ('print (spam [:2])')
print ('print (spam [1:])')
print ('print (spam [:])')

print ()
print ('Output:')
print ()

spam = ['cat', 'bat', 'rat', 'elephant']
print (spam [0:4])
print (spam [1:3])
print (spam [0:-1])
print (spam [:2])
print (spam [1:])
print (spam [:])

print ()
print ('len () can be used to get size of list:')

print ()
print ('Example:')
print ()

print ("spam = ['cat', 'dog', 'moose']")
print ('print (len (spam))')

print ()
print ('Output:')
print ()

spam = ['cat', 'dog', 'moose']
print (len (spam))

print ()
print ('Use index to change value in a list')
print ('Use + to concatenate lists')
print ('Use * to replicate lists')
print ('Use del to remove elements from list or delete the list itself')

print ()
print ('Example:')
print ()

print ("spam = ['cat', 'bat', 'rat', 'elephant']")
print ('del spam [2]')
print ('print (spam)')

print ()
print ('Output:')

print ()
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print (spam)

print ()
print ('range (len (somelist)):')

print ()
print ('Example:')
print ()

print ("supplies = ['pens', 'staplers', 'flame-throwers', 'binders']")
print ('for i in range (len (supplies)):')
print ("   print('Index ' + str(i) + ' in supplies is: ' + supplies[i])")

print ()
print ('Output:')
print ()

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range (len (supplies)):
   print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print ()
print ('in and not in operators:')

print ()
print ('Example:')
print ()

print ("print (('howdy' in ['hello', 'hi', 'howdy', 'heyas']))")
print ("spam = ['hello', 'hi', 'howdy', 'heyas']")
print ("print (('cat' in spam))")
print ("print (('howdy' not in spam))")
print ("print (('cat' not in spam))")

print ()
print ('Output:')
print ()

print (('howdy' in ['hello', 'hi', 'howdy', 'heyas']))
spam = ['hello', 'hi', 'howdy', 'heyas']
print (('cat' in spam))
print (('howdy' not in spam))
print (('cat' not in spam))

print ()
print ('Multiple assignnment trick:')

print ()
print ('Example:')
print ()

print ("cat = ['fat', 'black', 'loud']")
print ('size, color, disposition = cat')
print ("print (size + ' ' + color + ' ' + disposition)")

print ()
print ('Output:')
print ()

cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print (size + ' ' + color + ' ' + disposition)

print ()
print ('Augmented Assignment Operators:')
print ('1. += Also works for strings')
print ('2. -=')
print ('3. *= Also works for strings')
print ('4. /=')
print ('5. %=')


print ()
print ('Methods:')
print ('list.index ()')

print ()
print ('Example:')
print ()

print ("spam = ['hello', 'hi', 'howdy', 'heyas']")
print ("print (spam.index('hello'))")
print ("print (spam.index('heyas'))")
print ("szString = 'howdy howdy howdy'")
print ('try:')
print ('   spam.index(szString)')
print ('except:')
print ("   print (szString + ' is not in the list')")

print ()
print ('Output:')
print ()

spam = ['hello', 'hi', 'howdy', 'heyas']
print (spam.index('hello'))
print (spam.index('heyas'))
szString = 'howdy howdy howdy'
try:
   spam.index(szString)
except:
   print (szString + ' is not in the list')

print ()
print ('list.append () & list.insert ()')

print ()
print ('Examples:')
print ()

print ("spam = ['cat', 'dog', 'bat']")
print ('print (spam)')
print ("spam.append('moose')")
print ('print (spam)')
print ("spam.insert(1, 'chicken')")
print ('print (spam)')

print ()
print ('Output:')
print ()

spam = ['cat', 'dog', 'bat']
print (spam)
spam.append('moose')
print (spam)
spam.insert(1, 'chicken')
print (spam)

print ()
print ('del list[index] & list.remove ()')

print ()
print ('Examples:')
print ()

print ("spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']")
print ('print (spam)')
print ("spam.remove ('cat') # Only the first occurance is deleted")
print ('print (spam)')
print ('del spam [3]')
print ('print (spam)')

print ()
print ('Output:')
print ()

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
print (spam)
spam.remove ('cat')
print (spam)
del spam [3]
print (spam)

print ()
print ('list.sort () & list.sort (key=str.lower)')
print ('   Cannot sort if numbers and strings in same list')
print ('   Default is ASCIIbetical order (Z before a)')

print ()
print ('Examples:')
print ()

print ('spam = [2, 5, 3.14, 1, -7]')
print ('print (spam)')
print ('spam.sort()')
print ('print (spam)')
print ("spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']")
print ('print (spam)')
print ('spam.sort()')
print ('print (spam)')
print ('spam.sort(reverse=True)')
print ('print (spam)')
print ("spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']")
print ('print (spam)')
print ('spam.sort()')
print ('print (spam)')
print ("spam = ['a', 'z', 'A', 'Z', 'B', 'Y', 'b', 'y']")
print ('print (spam)')
print ('spam.sort(key=str.lower)')
print ('print (spam)')

print ()
print ('Output:')
print ()

spam = [2, 5, 3.14, 1, -7]
print (spam)
spam.sort()
print (spam)
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print (spam)
spam.sort()
print (spam)
spam.sort(reverse=True)
print (spam)
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
print (spam)
spam.sort()
print (spam)
spam = ['a', 'z', 'A', 'Z', 'B', 'Y', 'b', 'y']
print (spam)
spam.sort(key=str.lower)
print (spam)

print ()
print ('\ can be used as a continuation character')

print ()
print ('List-like Types:  Strings:')

print ()
print ('Example:')
print ()

print ("name = 'Zophie'")
print ('print (name [0])')
print ('print (name [-2])')
print ('print (name [0:4])')
print ("print (('Zo' in name))")
print ("print (('z' in name))")
print ("print (('p' not in name))")
print ('for i in name:')
print ("   print ('* * * ' + i + ' * * *')")

print ()
print ('Output:')
print ()

name = 'Zophie'
print (name [0])
print (name [-2])
print (name [0:4])
print (('Zo' in name))
print (('z' in name))
print (('p' not in name))
for i in name:
   print ('* * * ' + i + ' * * *')

print ()
print ('Slice strings:')

print ()
print ('Example:')
print ()

print ("name = 'Zophie a cat'")
print ('print (name)')
print ("newName = name [0:7] + 'the' + name [8:12]")
print ('print (name)')
print ('print (newName)')

print ()
print ('Output:')
print ()

name = 'Zophie a cat'
print (name)
newName = name [0:7] + 'the' + name [8:12]
print (name)
print (newName)

print ()
print ('tuple data type:')
print ('   parenthesis instead of square brackets')
print ('   requires tailing comma for list of one')

print ()
print ('Examples:')
print ()

print ("eggs = ('hello', 42, 0.5)")
print ('print (eggs)')
print ('print (eggs [0])')
print ('print (eggs [1:3])')
print ('print (len (eggs))')
print ("print (type (('hello',)))")
print ("print (type (('hello')))")

print ()
print ('Output:')
print ()

eggs = ('hello', 42, 0.5)
print (eggs)
print (eggs [0])
print (eggs [1:3])
print (len (eggs))
print (type (('hello',)))
print (type (('hello')))

print ()
print ('list () and tuple ()')

print ()
print ('Examples:')
print ()

print ("print (tuple (['cat', 'dog', 5]))")
print ("print (list (('cat', 'dog', 5)))")
print ("print (list ('hello'))")

print ()
print ('Output:')
print ()

print (tuple (['cat', 'dog', 5]))
print (list (('cat', 'dog', 5)))
print (list ('hello'))

print ()
print ('lists are references')

print ()
print ('Example:')
print ()

print ("spam = [0, 1, 2, 3, 4, 5]")
print ("print (spam)")
print ("cheese = spam")
print ("print (cheese)")
print ("cheese[1] = 'Hello!'")
print ("print (spam)")
print ("print (cheese)")

print ()
print ('Output:')
print ()

spam = [0, 1, 2, 3, 4, 5]
print (spam)
cheese = spam
print (cheese)
cheese[1] = 'Hello!'
print (spam)
print (cheese)

print ()
print ('Passing references')

print ()
print ('Example:')
print ()

print ("def eggs (someParameter):")
print ("   someParameter.append ('Hello')")
print ("spam = [1, 2, 3]")
print ("print (spam)")
print ("eggs (spam)")
print ("print (spam)")

print ()
print ('Output:')
print ()

def eggs (someParameter):
   someParameter.append ('Hello')
spam = [1, 2, 3]
print (spam)
eggs (spam)
print (spam)

print ()
print ('copy.copy () and copy.deepcopy ()')
print ('   Use copy.deepcopy if list contains lists')

print ()
print ('Example:')
print ()

print ("import copy")
print ("spam = ['A', 'B', 'C', 'D']")
print ("print (spam)")
print ("cheese = copy.copy(spam)")
print ("print (cheese)")
print ("cheese[1] = 42")
print ("print (spam)")
print ("print (cheese)")

print ()
print ('Output:')
print ()

import copy
spam = ['A', 'B', 'C', 'D']
print (spam)
cheese = copy.copy(spam)
print (cheese)
cheese[1] = 42
print (spam)
print (cheese)

print ()
print ('----- Chapter Five:  Dictionaries and Structuring Data -----')

print ()
print ('A dictionary is typed with braces {}')

print ()
print ('Example:')
print ()

print ("myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}")
print ("print (myCat)")
print ("print (myCat ['size'])")
print ("print ('My cat has '+ myCat ['color'] + ' fur.')")

print ()
print ("Output:")
print ()

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print (myCat)
print (myCat ['size'])
print ('My cat has '+ myCat ['color'] + ' fur.')

print ()
print ('Dictionaries can use integers as keys')

print ()
print ("Example:")
print ()

print ("spam = {12345: 'Luggage Combination', 42: 'The Answer'}")

print ()
print ("Dictionaries are unordered (unlike lists)")
print ("Dictionaries cannot be sliced like lists")

print ()
print ("Example:")
print ()

print ("spam = ['cats', 'dogs', 'moose']")
print ("bacon = ['dogs', 'moose', 'cats']")
print ("print (spam)")
print ("print (bacon)")
print ("print (spam == bacon)")
print ("eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}")
print ("ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}")
print ("print (eggs)")
print ("print (ham)")

print ()
print ("Output:")
print ()

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print (spam)
print (bacon)
print (spam == bacon)
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print (eggs)
print (ham)
print (eggs == ham)

print ()
print ("KeyError for dictionaries")

print ()
print ("Example:")
print ()

print ("spam = {'name': 'Zophie', 'age': 7}")
print ("try:")
print ("   print (spam ['color'])")
print ("except:")
print ("   print ('There is no color key')")

print ()
print ("Output:")
print ()

spam = {'name': 'Zophie', 'age': 7}
try:
   print (spam ['color'])
except:
   print ('There is no color key')

print ()
print ("keys (), values (), items () - data types dict_keys, dict_values, dict_items")

print ()
print ("Examples:")
print ()

print ("spam = {'color': 'red', 'age': 42}")
print ("for v in spam.values ():")
print ("   print ('Value: ' + v)")
print ("for k in spam.keys ():")
print ("   print ('Key: ' + k)")
print ("for i in spam.items ():")
print ("   print ('Item: ' + i)")
print ("for k, v in spam.items ():")
print ("   print ('Key: ' + k + ' Value: ' + str (v))")

print ()
print ("Output:")
print ()

spam = {'color': 'red', 'age': 42}
for v in spam.values ():
   print ('Value: ' + str (v))
for k in spam.keys ():
   print ('Key: ' + k)
for i in spam.items ():
   print ('Item: ' + str (i))
for k, v in spam.items ():
   print ('Key: ' + k + ' Value: ' + str (v))

print ()
print ('Use "in" and "not in" to check for keys and values in dictionaries')

print ()
print ("Example:")
print ()

print ("spam = {'name': 'Zophie', 'age': 7}")
print ("print ('name' in spam.keys ())")
print ("print ('Zophie' in spam.values ())")
print ("print ('color' in spam.keys ())")
print ("print ('color' not in spam.keys ())")
print ("print ('color' in spam)" + " # short hand for key")

print ()
print ("Output:")
print ()

spam = {'name': 'Zophie', 'age': 7}
print ('name' in spam.keys ())
print ('Zophie' in spam.values ())
print ('color' in spam.keys ())
print ('color' not in spam.keys ())
print ('color' in spam)

print ()
print ("Dictionary method:  get (<key of value>, default of key not found)")

print ()
print ("Example:")
print ()

print ("picnicItems = {'apples': 5, 'cups': 2}")
print ("print ('I am bringing ' + str (picnicItems.get ('cups', 0)) + ' cups.')")
print ("print ('I am bringing ' + str (picnicItems.get ('eggs', 0)) + ' eggs.')")

print ()
print ("Output:")
print ()

picnicItems = {'apples': 5, 'cups': 2}
print ('I am bringing ' + str (picnicItems.get ('cups', 0)) + ' cups.')
print ('I am bringing ' + str (picnicItems.get ('eggs', 0)) + ' eggs.')

print ()
print ("Dictionary method:  setdefault (<key>, <value>)")

print ()
print ("Example:")
print ()

print ("spam = {'name': 'Pooka', 'age': 5}")
print ("spam.setdefault ('color', 'black')")
print ("print (spam)")
print ("spam.setdefault('color', 'white')")
print ("print (spam)")

print ()
print ("Output:")
print ()

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault ('color', 'black')
print (spam)
spam.setdefault('color', 'white')
print (spam)

print ()
print ("Pretty printing")
print ("import pprint")
print ("pprint.pprint () and pprint.pformat ()")
print ("   pprint () prints")
print ("   pformat () just formats and returns a string")

print ()
print ("Example (functionally the same):")
print ()

print ("pprint.pprint(someDictionaryValue)")
print ("print(pprint.pformat(someDictionaryValue))")

print ()
print ("Nested Dictionaries and Lists")

print ()
print ("Example:")
print ()

print ("allGuests = {'Alice': {'apples': 5, 'pretzels': 12},")
print ("             'Bob': {'ham sandwiches': 3, 'apples': 2},")
print ("             'Carol': {'cups': 3, 'apple pies': 1}}")
print ()
print ("def totalBrought (guests, item):")
print ("   numBrought = 0")
print ("   for k, v in guests.items ():")
print ("      numBrought = numBrought + v.get (item, 0)")
print ("   return numBrought")
print ()
print ("print('Number of things being brought:')")
print ("print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))")
print ("print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))")
print ("print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))")
print ("print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))")

print ()
print ("Output:")
print ()

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought (guests, item):
   numBrought = 0
   for k, v in guests.items ():
      numBrought = numBrought + v.get (item, 0)
   return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

print ()
print ("Search for a key and a value:")

print ()
print ("Example:")
print ()

print ("spam = {'cat': 'food'}")
print ("if ('cat' in spam):")
print ("   print ('Found key')")
print ("if ('cat' in spam.keys ()):")
print ("   print ('Also found key')")
print ("if ('cat' not in spam.values ():")
print ("   print ('No value found')")

print ()
print ("Output:")
print ()

spam = {'cat': 'food'}
if ('cat' in spam):
   print ('Found key')
if ('cat' in spam.keys ()):
   print ('Also found key')
if ('cat' not in spam.values ()):
   print ('No value found')

print ()
print ('----- Chapter Six:  Manipulating Strings -----')

print ()
print ("\\' - Single quote")
print ('\\" - Double quote')
print ("\\t - Tab")
print ("\\n - Newline (line break)")
print ("\\\\ - Backslash")

print ()
print ("You can place an r before the beginning quotation mark of a string to make it a raw string.")
print ("The 'r' must come right before the single quote - no spaces allows.  Doesn't work for double quotes.")

print ()
print ("Example:")
print ()

print (r"print(r'That is Carol\'s cat.')")

print ()
print ("Output:")
print ()

print (r'That is Carol\'s cat.')

print ()
print ("A multiline string in Python begins and ends with either three single quotes or three double quotes.")
print ('Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string.')
print ("Python’s indentation rules for blocks do not apply to lines inside a multiline string.")

print ()
print ("Example:")
print ()

print ("print('''Dear Alice,")
print ()
print ("Eve's cat has been arrested for catnapping, cat burglary, and extortion.")
print ()
print ("Sincerely,")
print ("Bob''')")

print ()
print ("Output:")
print ()

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

print ()
print (r'Use """ to begin and end multiline comments')

print ()
print ("Example:")
print ()

print ('"""This is a test Python program.')
print ('Written by Al Sweigart al@inventwithpython.com')
print ('This program was designed for Python 3, not Python 2.')
print ('"""')

print ()
print ("Example:")
print ()

print ("def spam ():")
print (r'   """This is a multiline comment to help')
print (r'   explain what the spam() function does."""')
print ("   print('Hello!')")
print ()
print ("spam ()")

print ()
print ("Output:")
print ()

def spam():
   """This is a multiline comment to help
   explain what the spam() function does."""
   print('Hello!')

spam ()

print ()
print ("Strings use indexes and slices the same way lists do.")

print ()
print ("Example:")
print ()

print ("spam = 'Hello world!'")
print ("print (spam [0])")
print ("print (spam [4])")
print ("print (spam [-1])")
print ("print (spam [0:5])")
print ("print (spam [:5])")

print ()
print ("Output:")
print ()

spam = 'Hello world!'
print (spam [0])
print (spam [4])
print (spam [-1])
print (spam [0:5])
print (spam [:5])
print (spam [6:])

print ()
print ("Example:")
print ()

print ("spam = 'Hello world!'")
print ("fizz = spam [0:5]")
print ("print (fizz)")

print ()
print ("Output:")
print ()

spam = 'Hello world!'
fizz = spam [0:5]
print (fizz)

print ()
print ("The in and not in operators can be used with strings just like with list values.")

print ()
print ("Example:")
print ()

print ("print ('Hello' in 'Hello World')")
print ("print ('Hello' in 'Hello')")
print ("print ('HELLO' in 'Hello World')")
print ("print ('' in 'spam')")
print ("print ('cats' not in 'cats and dogs')")

print ()
print ("Output:")
print ()

print ('Hello' in 'Hello World')
print ('Hello' in 'Hello')
print ('HELLO' in 'Hello World')
print ('' in 'spam')
print ('cats' not in 'cats and dogs')

print ()
print ("upper (), lower (), isupper (), islower () string methods")

print ()
print ("Example:")
print ()

print ("spam = 'Hello world!'")
print ("print (spam)")
print ("spam = spam.upper()")
print ("print (spam)")
print ("spam = spam.lower()")
print ("print (spam)")

print ()
print ("Output:")
print ()

spam = 'Hello world!'
print (spam)
spam = spam.upper()
print (spam)
spam = spam.lower()
print (spam)

