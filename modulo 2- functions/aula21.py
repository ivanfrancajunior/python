def soma (x,y):
    return x + y

def multiplica(x,y):
    return x * y

def executa(funcao, x):
     def inside(y):
         return funcao(x,y)
     return inside
    

multiplica_por_2 = executa(multiplica,2)
soma_5 = executa(soma,5)

print(multiplica_por_2(5),soma_5(5))