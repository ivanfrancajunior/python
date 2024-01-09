# intro try / except


number = input('Type any value\n')


try:
    number_float = float(number)

    print(f'The doble of {number} is {number_float * 2:.0f}')
except:
    print('Use only numbers please ')