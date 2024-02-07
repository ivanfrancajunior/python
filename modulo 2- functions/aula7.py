''' Sets - Conjuntos em Python (tipo set)
        https://brasilescola.uol.com.br/matematica/conjunto.htm
         
         Conjuntos são ensinados na matemática
         
         Representados graficamente pelo diagrama de Venn
        
        Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

        # Sets são eficientes para remover valores duplicados de iteráveis.
        # - Não aceitam valores mutáveis;
        # - Seus valores serão sempre únicos;
        # - não tem índexes;
        # - não garantem ordem;
        # - são iteráveis (for, in, not in)
'''
# Criando um set
# set(iterável) ou {1, 2, 3}

s1 = set('Jota')

s1 = set()  # vazio

s1 = {'Jota', 1, 2, 3}  # com dados


# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Jota')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Jota')
print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)