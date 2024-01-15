'''
Python got drunk and the built-in functions str() and int() are acting odd:

You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.

https://edabit.com/challenge/pfn6QRn6eiTHEPpSs

'''

def int_to_str(args):
    return f'"{args}"'

def str_to_int(args):

    alg = ''
    i=0
    for number in args: 
        alg += f"{number[i]}"
    return int(alg) 

foury_seven = int_to_str(47)

print(foury_seven, type(foury_seven))


numebr_foury_seven = str_to_int("47")

print(numebr_foury_seven, type(numebr_foury_seven))

la = 'kasdknas'

def string_pairs(string):
    result = [string [i:i+2] for i in range(0, len(string), 2)]
    return result

print(string_pairs(la))
