# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
 
from datetime import datetime
from pytz import timezone



# dia_atual = datetime(2024,2,20,18,2,00,tzinfo=timezone('Asia/Tokyo'))
# print('dia_atual ->',dia_atual)

dia = datetime.now(timezone('America/Sao_Paulo'))
print('dia ->',dia)



# comparando datas: 

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('16/02/1994 09:30:30', fmt)

data_atual = data_fim = datetime.strptime('20/02/2024 18:27:20', fmt)

delta = data_atual - data_inicio #time delta

print('days -> ',delta.days,'sec -> ', delta.total_seconds())