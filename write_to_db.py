from sqlalchemy import create_engine, text, Column, inspect
import pandas as pd
import os
from dotenv import load_dotenv

#  Данные для БД
# Получаем учетные данные
load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_url = os.getenv('DB_URL')
db_port = os.getenv('DB_PORT')
db_name = "homeworks"
table_name = "komarov"

# Загружаем данные
script_path = os.path.dirname(os.path.abspath(file))
data_path = os.path.join(script_path, "data", "raw_data.parquet")
df = pd.read_parquet(data_path)
df = df.head(100)

# Подключаемся к homeworks
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"
)

# Проверяем подключение
with engine.connect() as conn:
    print("Успешное подключение")

# Записываем данные
df.to_sql(
    name=table_name,
    con=engine,
    schema="public",
    if_exists="replace",
    index=True
)
print("Данные успешно записаны в базу")

# Проверка
with engine.begin() as conn:
    conn.execute(text('ALTER TABLE public.komarov ADD PRIMARY KEY (index)'))

inspector = inspect(engine)
columns = inspector.get_columns("komarov", schema="public")

print("\nСтруктура таблицы:")
print({col["name"]: col["type"] for col in columns})
