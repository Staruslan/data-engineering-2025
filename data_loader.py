import pandas as pd

FILE_ID = "1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq"  # ID файла на Google Drive
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url, on_bad_lines='skip') # Читаем CSV-файл с Google Диска
print(raw_data.head(10)) #вывод 
