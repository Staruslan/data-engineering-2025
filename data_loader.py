import pandas as pd
import requests
from io import StringIO

url='https://drive.google.com/file/d/1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq/view?usp=share_link'

file_id = url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
url2 = requests.get(dwn_url).text
csv_raw = StringIO(url2)
raw_data = pd.read_csv(csv_raw)

# print('Переменные:',raw_data.columns)

# достаем имя переменных
size_perm = len(list(raw_data.columns)) # количество переменных в таблице
print('Количество переменных',size_perm)


for i in range(0, size_perm - 1, 1):
    print('Переменная',list(raw_data)[i], 'Тип переменной', (raw_data[list(raw_data)[i]].values).dtype)

# Сохранение итогового DataFrame в формате Parquet
raw_data.to_parquet('C:/Users/komar/my_project/raw_data.parquet', index=False)
print('Данные успешно сохранены в формате Parquet: raw_data.parquet')

