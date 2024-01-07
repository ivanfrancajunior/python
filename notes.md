## Basics: 

#### Comentários: 

``` python

# comentário

"""
DocString
"""

```


#### Tipos de dados:

#### Strings

- Representam um conjunto de caracteres.
- Devem ser escritos entre aspas
 
```python 

# strings 
string = 'sou uma string'

# escapes -> usados para skipar algum caracter especial `\` ou `r` 

print('Lil\' Vinicin ')



```

#### Numbers

- Representam tipos numéricos, divididos entre `int` e `float`
  
``` python 

# int -> numeros inteiros 
print(1)

# float -> numeros de ponto flutuante ou decimais 
print(1.2)

```

#### Booleans

- Seguindo a logica booleana indicam se algo é verdadeiro `True` ou falso `False`.

``` python 

print(10 == 10) # output: True

print(10 < 11) # output: False
```

#### Função `print`:

* Usada para dar um  output ao trecho de código.
* A função suporta mais de um parâmetro
* A separação dos valores passados podem ser definidos com o valor de `sep`.

```python 

'''
(function) def print(  
*values: object,  
sep: str | None = " ",  
end: str | None = "\n",  
file: SupportsWrite[str] | None = None,  
flush: Literal[False] = False  
) -> None
'''

print('Hello World!') # imprime Hello World no terminal ou no output selecionado

```

#### Função `type`:

- Usado pra checar o tipo de algum dado. 
  
```python 

print(type(1)) # <class 'int'>

print(type(1.0)) # <class 'float'>

print(type('string')) # <class 'str'>

print(type(False)) # <class 'bool'>
```

#### Função Coercion ou Conversão de Tipos:

- É o ato de converter um tipo em outro
- Funciona em tipos primitivos. 
  
```python

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

```

#### Variáveis: 

* Variáveis são usadas para salvar algo na memória do computador.

```python
nome = 'Jota Apenas'
```

#### Formatação de Strings: `f-strings`

- Em Python, as f-strings (format strings) fornecem uma maneira concisa e poderosa de formatar strings. 
- Elas são criadas prefixando uma string com o caractere 'f' ou 'F' e permitem a incorporação de expressões dentro da própria string.



```python

nome = 'Jota'
idade = 29

info_user = f'Este é {nome}, ele tem {idade} anos ' # vc ja entendeu n vô escrever ;)  

```

#### Formatação de Strings: `.format()`

- O método `format` em Python é outra maneira de formatar strings
- Os pares de chaves assumem respectivamente os valores passados ao método 

```python
nome = "Bob"
idade = 30
altura = 1.75

mensagem = "{} tem {} anos e mede {} metros.".format(nome, idade, altura)

print(mensagem) # "Bob tem 30 anos e mede 1.75 metros."

```