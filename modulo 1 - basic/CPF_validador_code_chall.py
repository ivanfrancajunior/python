"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

868.278.680-01

1- multiplicar pelo fatorial de 10 até 2   
10 54 40 35 0 0 8 24 14 

2 - somar todos os resultados anteriores

10+54+40+35+0+0+8+24+14 = 165

3 - multiplicar o resultado anterior por 10 e obter o resto da divisão por 11

165*10 = 1650 % 11 = 5

"""

import re
import random

cpf='161.728.680-04'

valid_cpf = re.sub(r'[^0-9]','',cpf)

first_nine_digits = valid_cpf[:9]

first_ten_digits = valid_cpf[:10]

print(first_nine_digits)

def calulateFirstDigit(number):
    start = 10
    count =0    
    for i in range(0,9):
      count += (int(first_nine_digits[i]) * start)
      start -= 1

    digit = (count * 10) % 11

    valid_digit = digit if digit <= 9 else 0
    
    return  valid_digit

print(calulateFirstDigit(first_nine_digits))   

def calculateSecondDigit(number):
    start = 11
    count =0    
    for i in range(0,10):
      count += (int(first_ten_digits[i]) * start)
      start -= 1

    digit = (count * 10) % 11

    valid_digit = digit if digit <= 9 else 0
    
    return  valid_digit

print(calculateSecondDigit(first_ten_digits))   
 

def validade_cpf(cpf):

    first_digit = calulateFirstDigit(cpf)
    second_digit = calculateSecondDigit(cpf)

    if first_digit == int(cpf[9]) and second_digit == int(cpf[10]):
        return print(f'{cpf} Is a valid cpf.')
    return print(f'{cpf} Isn\'t a valid cpf')

validade_cpf(valid_cpf)

def cpf_generator():
   
   first_eigth =''
   nineth_digit = '' 
 
   for i in range(9):
      first_eigth+= str(random.randint(0,9))
    
   nineth_digit = str(calulateFirstDigit(first_eigth))

   last_digit = str(calculateSecondDigit(nineth_digit))

   full_cpf = int(first_eigth + nineth_digit + last_digit)

   return full_cpf



validade_cpf(str(cpf_generator()))


