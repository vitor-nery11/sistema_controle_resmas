from datetime import datetime 
data = '29/06/2026'

data_valida = datetime.strptime(data, '%d/%m/%Y')

print(data_valida)