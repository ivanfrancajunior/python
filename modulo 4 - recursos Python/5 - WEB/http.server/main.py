'''
     HTTP PRPTOCOL  (HyperText Transfer Protocol)

    HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
    dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
    (seu navegador, por exemplo) faz uma requisição ao servidor
    (site, por exemplo), que responde com os dados adequados.

    A mensagem de requisição do cliente deve incluir dados como:
    - O método HTTP
        - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
        - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
    - O endereço do recurso a ser acessado (/users/)
    - Os cabeçalhos HTTP (Content-Type, Authorization)
    - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)

    A mensagem de resposta do servidor deve incluir dados como:
    - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    - Os cabeçalhos HTTP (Content-Type, Accept)
    - O corpo da mensagem (Pode estar em vazio em alguns casos)

'''

# requests + Beautifulsoup4

import requests

from bs4 import BeautifulSoup

def extract(page : int=0):

    headers ={"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}

    url = f'https://books.toscrape.com/'
   
    raw_response = requests.get(url, headers)

    response = BeautifulSoup(raw_response.text, 'html.parser')

    return response

first = extract()


def traits_one(response:BeautifulSoup):

    links_collection:list[str] = []

    divs = response.find_all('article', class_ = 'product_pod',)
    
    

    for items in divs:
    
        link = items.find('a') 

        links_collection.append(link)
    
    return links_collection


second = traits_one(first)


# print(second, sep=' \n')

def write_in_md_file(list_of_title:list[str]):
    file_path = "my_list_of_books.md"
    i = 1
    with open(file_path,'w+', encoding="utf8" ) as list_of_books:
        
        for title in list_of_title:

            list_of_books.write(f"#{ i } - {title} \n")   

        i+= 1
    print("done!")   

write_in_md_file(second)