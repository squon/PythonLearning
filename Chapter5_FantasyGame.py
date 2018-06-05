#! /usr/bin/python3
#

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory (inventory):
   print ("Inventory:")
   print ()
   itemCount = 0
   for key, value in (inventory.items ()):
      # print (key + ": " + str (value))
      print (str (value) + " " + key)
      itemCount += value
   print ()
   print ("Total number of items: " + str(itemCount))

print ()
displayInventory (inventory)

#
# Part two
#
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory (inventory, addedItems):
   for item in addedItems:
      # itemCount = inventory.get (item, 0) + 1
      # print (itemCount)
      # inventory [item] += str ((int (inventory [item])) += 1)
      inventory [item] = inventory.get (item, 0) + 1

def addWhat (dragonLoot):
   for item in dragonLoot:
      print ("Adding " + item)

print ()
addWhat (dragonLoot)
addToInventory (inventory, dragonLoot)

print ()
displayInventory (inventory)

