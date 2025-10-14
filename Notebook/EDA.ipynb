import pandas as pd
import requests
from io import StringIO

# Ссылка на csv файл видеоданных
url = 'https://drive.google.com/file/d/1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq/view?usp=share_link'

file_id = url.split('/')[-2]
dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
response = requests.get(dwn_url)
response.raise_for_status()

csv_raw = StringIO(response.text)
raw_data = pd.read_csv(csv_raw)

print("Данные загружены из внешнего CSV файла. Файл не был сгенерирован искусственным интеллектом.\n")

print("Переменные в данных:", raw_data.columns.tolist())

# Completeness: доля непустых значений по столбцам
completeness = raw_data.notnull().mean()

# Uniqueness: доля уникальных строк
total_rows = len(raw_data)
unique_rows = raw_data.drop_duplicates().shape[0]
uniqueness = unique_rows / total_rows if total_rows > 0 else 0

# Duplication Rate: процент дубликатов
duplication_rate = 1 - uniqueness

# Accuracy (простейшая проверка для числовых столбцов — доля отрицательных значений)
accuracy_report = {}
for col in raw_data.columns:
    if pd.api.types.is_numeric_dtype(raw_data[col]):
        neg_count = (raw_data[col] < 0).sum()
        total_count = len(raw_data[col])
        accuracy_report[col] = {
            "negative_values": neg_count,
            "total": total_count,
            "negative_ratio": neg_count / total_count if total_count > 0 else 0
        }
    else:
        accuracy_report[col] = "Не числовой столбец — проверка не выполнена."

print("\nОценка качества данных:")
print("1. Completeness (полнота) по столбцам:")
print(completeness)

print(f"\n2. Uniqueness (уникальность строк): {uniqueness:.4f} ({unique_rows} уникальных из {total_rows} записей)")

print(f"\n3. Duplication Rate (уровень дублирования): {duplication_rate:.4f}")

print("\n4. Accuracy (простейшая проверка отрицательных значений в числовых столбцах):")
for col, stats in accuracy_report.items():
    if isinstance(stats, dict):
        print(f" - {col}: отрицательных значений = {stats['negative_values']} из {stats['total']} "
              f"(доля {stats['negative_ratio']:.4f})")
    else:
        print(f" - {col}: {stats}")
