#Basic string operations
str = 'Hello World, this is a string!'

print(len(str)) #Get length
print(str * 3) #Repeat
print(str.replace('Hello', 'Hola')) #Replace
print(str.split(',')) #Split string, put the split strings into a list
print(str.startswith('H')) #Does string start with ___? Returns boolean
print(str.endswith('!')) #Does string end with ___? Returns boolean
print(str.upper()) #makes all char uppercase
print(str.lower()) #makes all lowercase
print(str.capitalize())

#Slicing - or getting a substring
print(str[0:5]) #Get the first 5 [start:end]
print(str[6:]) #Get the 6th to the end
print(str[-7:]) #Get the last 7, counts backwards
print(str[6:11]) #Get the 6 to BEFORE 11

#Indexes - the position of char
l = ','
c = str.find(l) # c = -1 if not found
print(f'Find returned {c}')

i = str.index(l) #WILL JUST THROW ERROR IF SUBSTRING IS NOT IN STRING BUT find() RETURNS -1
print(f'Find returned {i}')

#Creating new string from substring
x = str[:i] #Creates new string from substring of start to i exclusive 
print(x)


