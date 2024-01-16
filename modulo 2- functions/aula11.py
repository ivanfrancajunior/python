# lambda function


def executa(fn, *args):
    
    return fn(*args)

print(executa(lambda x,y: x + y, 2,3))