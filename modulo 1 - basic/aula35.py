"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""
import os
palavra_secreta = 'lasanho'

letras_acertadas = ''
contador_tentativas = 0

while True:

    letra_digitada = input('Digite uma letra : \n')
    
    if len(letra_digitada) > 1: 
        print('Digite apenas uma letra por vez.')
        continue

    contador_tentativas += 1
    
    if letra_digitada in palavra_secreta:

        letras_acertadas += letra_digitada 

    palavra_formada_atual = ''

    for letra_descoberta in palavra_secreta:

        if letra_descoberta in letras_acertadas:

            palavra_formada_atual += letra_descoberta

        else: 
            palavra_formada_atual += "*"

    print('Palavra formada: ', palavra_formada_atual)

    if palavra_formada_atual == palavra_secreta:
        
        os.system("cls")

        print('VOCÊ GANHOU!!!')
        
        print("A palavra era: ", palavra_secreta)
        
        print('Você tentou', contador_tentativas, 'vezes.')
    
        letras_acertadas = ''
        numero_tentativas = 0
    