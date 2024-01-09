# exercicio 1

name = 'Jota'
idade= 30
ano_nascimento = 2024 - idade
maior_de_idade = idade >= 30
altura_metros = 1.73

print('Nome', name,'\nIdade:', idade, "\nAno de Nascimento:",ano_nascimento, "\nMaior de idade?",maior_de_idade, "\nAltura em metros:", altura_metros,'m' )


# exercicio 2
 
peso = 60
altura = 1.73

imc = peso / altura ** 2

print(name, imc, sep='-')

info_imc = '{} tem {} kilos, mede {} metros e seu imc tem valor de {:.2f}'.format(name,peso, altura,imc)

print(info_imc)

newname = input('Qual seu nome? \n')

print(f"Olá camarada {newname=}!")
