#Sets {}
#Sets contain unordered (can't control order), unique (can't have multiple of the same thing), immutable (cannot change, can only add/remove elements) data types in a hash table
#s = {1,2,2,2,3,4,5}
#print(s) #scripts out the extra 2s

l = ['Sharon', 'Oh', 17]
s = set(l) #converts data type to set
print(s) #elements put in random order

#Add items
s.add('Hello')
s.update([4, 5, 6, 'Hello']) #another way, unique items only
print(s)

#Remove items
s.discard('Hello') #if element does not exist, will NOT throw error
s.remove(4) #if element does not exist, will throw error
v = s.pop() #Removes whatever item and gives it to you (random in sets)
print(s)

#Cannot change items in a set directly INSTEAD you have to remove then add
#s[0] = 'A'
#print(s[0])
#both throw error, CAN'T INDEX IN A SET
s.remove(6)
s.add(4)
print(s)


