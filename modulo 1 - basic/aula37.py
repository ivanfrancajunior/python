"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []


while True:
    
    print('Selecione uma opção')
    
    opcao = input('[L]istar, [I]nserir, [A]pagar \n')

    # if len(opcao) > 1 :
    #     print('Digite uma opção válida.')
    #     continue

    # if opcao != 'I' or opcao !="L" or opcao !='A':
    #     print('Digite uma opçãp válida')
    #     continue
    
    if len(lista) == 0 and opcao == 'l':
        os.system('cls')
        
        print('A lista atual está vazia')
        
        continue

    if opcao == 'i':
        os.system('cls')
        
        item = input('Informe o item. \n')
        
        lista.append(item)

        print(f'O item "{item}" foi adicionado.')
        
        continue
    
    elif opcao == 'l':
        
        os.system('cls')
        
        for indice, item in enumerate(lista):
           
            print(indice + 1, item, sep = ' - ' )
            
        continue

    elif opcao == 'a':
        
        if len(lista) == 0:
            print('A lista atual está vazia')
            continue

        
        item_or_indice = input("Insira o nome do item ou o numero da listagem.")

        try:
            indice = int(item_or_indice)

            if 1 <= indice <= len(lista):
                
                # Remover pelo índice
               
                removido = lista.pop(indice - 1)
                
                os.system('cls')
                
                print(f'{removido} foi removido da lista pelo índice {indice}')
            else:
                print('Índice inválido, tente novamente.')
        except ValueError:

            # Remover pelo nome

            if item_or_indice in lista:

                lista.remove(item_or_indice)
                
                os.system('cls')
                print(f'{item_or_indice} foi removido da lista pelo nome')
            else:
                print('Item não encontrado, tente novamente.')
        
        continue
    
    else:
        print('Opção inválida.')

        continue
