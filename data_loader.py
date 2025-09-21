import pandas as pd

FILE_ID = "1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq"  # ID файла на Google Drive
file_url = f"https://drive.google.com/file/d/1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq/view?usp=drive_link={FILE_ID}"

raw_data = pd.read_csv(file_url)     # читаем файл
print(raw_data.head(10))         # выводим на экран первые 10 строк для проверки
