import csv
import random
from datetime import datetime, timedelta

# Configurações
equipment_ids = [f"EQ-{str(i).zfill(2)}" for i in range(1, 205)]  # EQ-01 a EQ-205
start_date = datetime(2023, 1, 1)
num_rows = 5000

# Função para gerar timestamp com fuso horário
def random_timestamp_with_timezone(start, end):
    # Gera um timestamp aleatório
    timestamp = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    # Formata como string com milissegundos e fuso horário -05:00
    return timestamp.strftime('%Y-%m-%dT%H:%M:%S.000-05:00')

# Criar o arquivo CSV
with open('equipment_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    
    # Escreve o cabeçalho
    csvwriter.writerow(['equipmentId', 'timestamp', 'value'])
    
    for _ in range(num_rows) - 1:
        equipment_id = random.choice(equipment_ids)
        timestamp = random_timestamp_with_timezone(start_date, datetime.now())
        value = round(random.uniform(20, 40), 2)  # Valores aleatórios entre 20 e 40
        csvwriter.writerow([equipment_id, timestamp, value])

print("CSV gerado com sucesso!")
