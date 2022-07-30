#Strings
for x in 'hello':
    print(f'{x} = {ord(x)}')

#How to make a string
first = "Sharon"
last = "Oh"
print(first + ' ' + last)
print(f'Hello my name is {first} {last}') #Use format to avoid issues, use {} to print variable value with format

hers = "Heather's"
print(hers)

#Under the hood of strings
#A string is a unicode/sequence of one or more characters

s1 = chr(72) #num represent characters, also for upper and lower case
s2 = chr(105)
print(s1 + s2)
print(chr(8710)) #math symbols too!!

#Escape characters - start with a slash \
print(f'Hello{chr(13) + chr(10)}World')
print(f'Hello\r\nWorld')

strTest = "Hello\tWorld"
print(strTest)

hers = 'Heather\'s'
print(hers)

quote = "Then he said \"hello\" to me"
print(quote)

#Must format strings to avoid errors
name = "Sharon"
age = 17
#print(name + ' ' + age) ERROR!!!
print(f'My name is {name}. I am {age} years old')
print('My name is %s. I am %i years old' %(name,age)) # %s first string, %i first int










