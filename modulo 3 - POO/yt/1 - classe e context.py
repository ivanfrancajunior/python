class MinhaClasse():
    def __init__(self, nome,atributo) -> None:
        self.nome = nome
        self.atributo = atributo

    def metodo(self):
        print (f'{self.nome} {self.atributo}')

c1 = MinhaClasse('Classe 1', 'Algm atributo')

c1.metodo()


class ControleRemoto():
    canal = 1
    
    def __init__(self, marca, location) -> None:
        self.marca = marca
        self.location = location
    
    def avancar_canal(self):
        
        if self.canal == 'AV' or self.canal < 1:
            self.canal = 1
            return self.canal
        else:
            self.canal += 1
            return self.canal
    
    def voltar_canal(self):
        
        if self.canal == 1 :
            return "AV"
         
        self.canal -= 1 
        return self.canal
    
    def escolher_canal(self, valor):
        self.canal = valor
        return self.canal
    
samsung_tv_remote = ControleRemoto('Sansung', 'Sala')

print(samsung_tv_remote.canal)
print(samsung_tv_remote.voltar_canal())
print(samsung_tv_remote.avancar_canal())
print(samsung_tv_remote.avancar_canal())
print(samsung_tv_remote.escolher_canal(12))


