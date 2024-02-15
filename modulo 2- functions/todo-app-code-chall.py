# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

task_list = []

task_history = []
on = True

while on == True:
    
    opcoes = input('Selecione uma opcao: [A] Adicionar nova tarefa | [L] Listar suas tarefas [D] Desfazer ultima tarefa [R] Refazer ultima alteração [E] Sair \n')

    if opcoes.upper() == 'A':
        
        nova_tarefa = input('Insira sua tarefa: \n')
        
        if nova_tarefa == '':
            print('Tá bobo né mano... faz na moral ai! ')

        task_list.append(nova_tarefa)

    elif opcoes.upper() =='L':
        i = 1

        if len(task_list) < 1:
            print('Você ainda não adicionou uma tarefa.')

        for task in task_list: 
            print('-' * 20)
            print(f"{i} - {task}", sep='\n')
            print('-' * 20)
            i +=1
    elif opcoes.upper() =='D':

        last_task = task_list[len(task_list) - 1]

        print(last_task)
        task_list.pop()
        task_history.append(last_task) 
        print('Tarefa remocida com sucesso!')
    
    elif opcoes.upper() =='R':
        
        old_tasks = task_history
        
        if len(old_tasks) < 1:
            print('Não há mais tarefas no histórico.')
        
        last_task = old_tasks[len(old_tasks) - 1 ]

        task_list.append(last_task)
        
        old_tasks.pop()

        print('Tarefa adicionada com sucesso!')


    elif opcoes.upper() =='E':
        break
    else:
        
    
        print('Digite apenas opções válidas: [A] Adicionar | [L] Listar | [D] Desfazer alteração | [R] Refazer alteração | [E] Sair \n')

    # tarefa = input('Adicione uma tarefa\n')
