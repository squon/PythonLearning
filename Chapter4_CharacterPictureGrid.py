#! /usr/bin/python3
#

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print (grid)
print (len (grid))
print (len (grid [0]))

for xaxis in range (0, (len (grid [0]))):
   for yaxis in range (0, (len (grid))):
      print (grid [yaxis][xaxis], end='')
   print ()
