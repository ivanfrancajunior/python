'''
    ARQUIVOS CSV  NO PYTHON  (Comma Separated Values - Valores separados por vírgulas)
    
    # É um formato de arquivo que armazena dados em forma de tabela, onde cada linha representa uma linha da tabela e as colunas são separadas por vírgulas.
    
    # Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
     plataformas, como por exemplo, para importar ou exportar dados para uma planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
    
    # Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um editor de texto ou em uma planilha eletrônica.

    # Um exemplo de um arquivo CSV pode ser:

    # Nome,Idade,Endereço
    # Luiz Otávio,32,"Av Brasil, 21, Centro"
    # João da Silva,55,"Rua 22, 44, Nova Era"

    # A primeira linha do arquivo define os nomes das colunas da, enquanto as linhas seguintes contêm os valores das linhas, separados por vírgulas.

    # Regras simples do CSV

    # 1 - Separe os valores das colunas com um delimitador único (,)
    
    # 2 - Cada registro deve estar em uma linha
    
    # 3 - Não deixar linhas ou espaços sobrando
    
    # 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

'''

from pathlib import Path
import csv

CSV_FILE_DIR = Path(__file__).parent/'file.csv'
CSV_FILE_WRITEBLE_DIR = Path(__file__).parent/'filewriteble.csv'

print(CSV_FILE_DIR)
print(CSV_FILE_WRITEBLE_DIR)

#LEITURA DE ARQUIVO
with open(CSV_FILE_DIR, 'r', encoding='utf8') as arquivo: 
    # formato de lista
    # reader = csv.reader(arquivo)
    # formato de dicionáriro
    reader = csv.DictReader(arquivo)
    for row in reader:
        
        print(row['Nome'], row['Idade'], row['Endereço']) 


clientes= [
    {'Nome': 'Joao da Silva', 'Email': 'emaildojoao@gmail.com' },
    {'Nome': 'Maria da Silva', 'Email': 'emaildamaria@gmail.com' },
    {'Nome': 'José da Silva', 'Email': 'emaildojose@gmail.com' },
    ]

#ESCRITA DE ARQUIVO
with open(CSV_FILE_WRITEBLE_DIR, 'w+', encoding="utf8") as arquivo:
    
    writer = csv.writer(arquivo)

    nome_colunas = ['Nome', 'Endereço']

    writer.writerow(nome_colunas) 

    for cliente in clientes:
        writer.writerow(cliente.values()) 

    print('Done!')

#escrevendo com dicionários
    
# with open(CSV_FILE_WRITEBLE_DIR, 'w') as arquivo:
#     
# nome_colunas = lista_clientes[0].keys()
#     escritor = csv.DictWriter(
#         arquivo,
#         fieldnames=nome_colunas
#     )
#     escritor.writeheader()

#     for cliente in lista_clientes:
#         print(cliente)
#         escritor.writerow(cliente)
