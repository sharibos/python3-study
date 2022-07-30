#Lists []
print('--------------------') #To signify start in Terminal
#Create a list - remember the square brackets
x = ['Sharon', "Oh", 17] #can mix data types in lists in Python
print(x)
print(f'List: {x}') #Print list
print(f'Length: {len(x)}') #Print length
print()

#Index and positioning
print(f'Zero: {x[0]}') #First item
print(f'Slice: {x[1:2]}') #Slice the list (2 is EXCLUSIVE, cuts off before 2)
print()

#Adding items - append, insert
x.append('Pizza')
x.append('Drink') #Added to end, in the order you append!
print(f'List: {x}')

x.insert(1, 'Cats') #Adds to specific position (index 1 now 'Cats')
print(f'List: {x}')
print()

#Removing items - remove, pop, delete
x.remove('Cats') #Removes first instance
print(f'List: {x}')

i = x.index('Pizza') #Error if not found btw
print(f'Food: {x.pop(i)}')
print(f'List: {x}') #Remove and return item

i = x.index('Drink') #Error if not found btw
del x[i] #Deletes specific item w/o returning it (NO MEMORY!)
print(f'List: {x}')
print()

#Extending - adds element from another list
y = ['Cats', 'Dogs', 'Birds']
x.extend(y) #Adds items of y to end of list x
print(f'Extend: {x}')
print()

#Sort - sort, reverse
x.remove(17) #because sort will throw an error with mixed types
x.sort() #Sorts alphabetically
print(f'Sort: {x}')

x.reverse() #Reversed alphabetical order
print(f'Reverse: {x}')
print()

#Copy
y = x.copy() #Copies the elements into a new list
y.reverse()
y.append('Apples')
print(f'Original: {x}')
print(f'New: {y}')
print()

#Delete the whole thing
del y

#Clear
x.clear() #empties list
print(f'Cleared: {x}')

#Lists can contain other lists
x = []
y = [1,2,3]
z = ['Sharon', 'Oh'] 
x.append(y)
x.insert(0,z)
print(f'List: {x}')
print(f'Length: {len(x)}')
print(f'0: {x[0]}')
print(f'1: {x[1]}')

print(f'0: {x[0][0]}') #Printing first element of first list
print(f'1: {x[1][1]}') #Printing second element of second list
print()

#Changing items - positional
x = [1,2,3,4,5]
x[2] = 'Test'
x[3] = '3'
print(x)
print()