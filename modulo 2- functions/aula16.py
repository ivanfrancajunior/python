# try, except, else e finaly
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# x = 1
# y = 0
# z = x / y
# print(z)

def divisao(a,b):
    try:
        result = a / b
        return result
        
    except ZeroDivisionError as err:
        print(err)
        return ('ta bobo cara?')
    
    except (NameError, IndexError) as err:
        return ('ta bobo cara?', err)
    

print(divisao(1,1))
print(divisao(1,0))
