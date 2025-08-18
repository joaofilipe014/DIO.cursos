# from datetime import date, datetime, time
#
# data = date(2025, 8, 12)
# print(data)
# print(date.today())
#
# data_hora = datetime(2025, 8, 12, 10, 30, 0)
# print(data_hora)
# print(datetime.now())
#
# time = time(20, 30, 0)
# print(time)

# from datetime import timedelta, datetime
#
# tipo_carro = "" #P,M,G
# tempo_Pequeno = 30
# tempo_Medio = 45
# tempo_Grande = 60
# data_atual = datetime.now()
#
# tipo_carro = input("\n Informe o tamanho do seu carro(P,M,G): ")
#
# if tipo_carro == 'P':
#     data_retirada = data_atual + timedelta(minutes = tempo_Pequeno)
#     print(f'O carro chegou: {data_atual} e ficará pronto em: {data_retirada}')
# elif tipo_carro == 'M':
#     data_retirada = data_atual + timedelta(minutes = tempo_Medio)
#     print(f'O carro chegou: {data_atual} e ficará pronto em: {data_retirada}')
# else:
#     data_retirada = data_atual + timedelta(minutes = tempo_Grande)
#     print(f'O carro chegou: {data_atual} e ficará pronto em: {data_retirada}')

# from datetime import datetime
# d_atual = datetime.now()
# date_string = "2025-08-12 10:30"
# mascara_ptbr = "%d/%m/%Y %a"
# mascara_en = "%Y-%m-%d %H:%M"
#
# print(d_atual.strftime(mascara_ptbr))
# data_convertida = datetime.strptime(date_string, mascara_en)
# print(data_convertida)
# print(type(data_convertida))

# Com pytz
# from datetime import datetime as dt
# import pytz

# Criando datatime com timezone
# d = dt.now(pytz.timezone('America/Sao_Paulo'))
# print(d) # 2025-08-13 15:19:00-03:00

# Sem pytz
from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=+2)))
data_SP = datetime.now(timezone(timedelta(hours=-3)))
print(data_oslo)
print(data_SP)