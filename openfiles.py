exmp2 = '/resources/data/Example2.txt'

with open('Example2.txt', 'w') as exmp2:
    exmp2.write("This is line C\n")
    exmp2.write("This is line D\n")
    exmp2.write("This is line E\n")

with open('Example2.txt', 'r') as exmp2:
    print(exmp2.read())

# r+ : Reading and writing. Cannot truncate/shorten the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists.
    