#Numbers - int float complex

#int (no decimal point)
iVal = 34
print(f'iVal = {iVal}')
    
#float (yes decimal point, kinda like a double??)
fVal = 3.14
print(f'fVal = {fVal}')
import sys
print(sys.float_info) #what's happening under the hood

#complex - complex(real, imag) (something else)
cVal = 3 + 6j
print(f'cVal = {cVal}')
cVal = complex(5,3)
print(f'cVal = {cVal}')
print(f'real = {cVal.real}, imag = {cVal.imag}')


#Basic numerical operations
x = 3
print(f'x = {x}')

y = x + 3 #add
print(f'add = {y}')

y = x - 1 #subtract
print(f'subtract = {y}')

y = x * 6.846 #multiply
print(f'multiply = {y}')

y = x / 0.5 #divide
print(f'divide = {y}')

y = x**2 #pow
print(f'pow = {y}')

y = x%2.5 #modulus (remainder)
print(f'remain = {y}')