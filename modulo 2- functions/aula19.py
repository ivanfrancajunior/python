"""# Modularização - Entendendo os seus próprios módulos Python

# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

"""

import aula19b

print('Este módulo se chama', __name__)

print(aula19b.variavel)


"""
# Recarregando o módulo importlib.reload

# para recarregar um módulo importlib.reload(nome_do_module) e é util para fazer reload de algum módulo caso seja necessário,

"""
# import importlib

# importlib.reload(aula19b)