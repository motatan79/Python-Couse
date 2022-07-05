
def roman_to_int(s):
    rom_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    int_val =0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
            int_val += rom_val[s[i]]
        if i > 0 and rom_val[s[i]] > rom_val[s[i -1]]:
            int_val += rom_val[s[i]]
        elif i >0 and rom_val[s[i]] < rom_val[s[i -1]]:
            int_val -= rom_val[s[i]]
        else:
            int_val = 1
    print(int_val)
    return int_val

roman_to_int('IX')


x = [28, 79, 19]
binario = []

for i in x:
    sum_digits = 0
    while i >= 1:
        sum_digits += i%2
        i = i // 2
    print('suma', sum_digits)
    binario.append(sum_digits)
print(binario)

lista = [z for z in list(zip(x, binario))]
print(lista)

lista2 = sorted(lista, key = lambda x : x[1])
print(lista2)


#
import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    hora = s[:2]
    time = s[:-2]
    print(time)
    if time == 'PM':
        nueva_hora = int(hora) + 12
    else:
        nueva_hora = int(hora)

    minutos = s[3:5]
    segundos = s[6:8]

    return f'{nueva_hora}:{minutos}:{segundos}'

s = '04:59:59AM'

# Write your code here
hora = s[:2]
time = s[-2:]

if time == 'PM' and int(hora) < 12:
    nueva_hora = int(hora) + 12
elif time == 'AM' and int(hora) == 12:
    nueva_hora = '00'
else:
    nueva_hora = hora

minutos = s[3:5]
segundos = s[6:8]

print(f'{nueva_hora}:{minutos}:{segundos}')


string = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']

contador = 0
'''lista = []
lista2 = []
for i in queries:
    rep = string.count(i)
    lista.append(rep)'''

lista = [string.count(x) for x in queries]
print(lista)


