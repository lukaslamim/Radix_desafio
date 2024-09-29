import csv
import random
from datetime import datetime, timedelta

# Configurações
equipment_ids = [f"EQ-{str(i).zfill(2)}" for i in range(1, 99)]  # EQ-01 a EQ-98
start_date = datetime(2023, 1, 1)
num_rows = 5000

# Função para gerar timestamp com fuso horário
def random_timestamp_with_timezone(start, end):
    timestamp = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return timestamp.strftime('%Y-%m-%dT%H:%M:%S.000-05:00')

# Criar o arquivo CSV
data = []
for _ in range(num_rows):
    equipment_id = random.choice(equipment_ids)
    timestamp = random_timestamp_with_timezone(start_date, datetime.now())
    value = round(random.uniform(20, 40), 2)
    data.append([equipment_id, timestamp, value])

# Gravação do arquivo CSV
with open('equipment_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(['equipmentId', 'timestamp', 'value'])
    
    for row in data:
        if isinstance(row, str):
                row.encode('utf-8')  
        csvwriter.writerow(row) 

print("CSV gerado com sucesso!")
