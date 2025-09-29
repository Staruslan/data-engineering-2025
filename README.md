# **Data Engineering (Project 2025)**

**Студент ПИШ ИТМО**: Комаров Руслан

**Преподаватель:** Пандаков Виктор Викторович
 ____

 
- Данные для исследования, запись передвижения биологического объекта (лабораторная мышь) приведена на рис.1.

- Ссылка на датасет: https://drive.google.com/drive/folders/17CqpL_vUcgqztIK5kGpLKhGqC8Ex8KJ-?usp=drive_link
    
- Скрипт [data_loader.py](https://github.com/Staruslan/data-engineering-2025/blob/main/data_loader.py) на Python для чтения датасета.
Данный скрипт работает в связке [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)+[poetry](https://python-poetry.org/docs/basic-usage/).

<img width="325" height="441" alt="image" src="https://github.com/user-attachments/assets/00d1d28e-0823-4e8e-9826-6977b9f85db0" />

Рисунок 1 - Лабораторная мышь при проведении теста


1. conda create -n my_env python=3.13 pip
2. conda activate my_env

3. pip install poetry
4. poetry new my_project

5. cd my_project
6. poetry add jupyterlab pandas matplotlib wget
7. poetry install —no-root


- Вывод файла зависимостей [pyproject.toml](https://github.com/Staruslan/data-engineering-2025/blob/main/pyproject.toml);

- Вывод первых 10 строк из наших данных на рис.2.

<img width="1915" height="660" alt="image" src="https://github.com/user-attachments/assets/f4fde124-de16-4bb8-b0a7-c7feaafd040c" />

Рисунок 2 - Вывод зависимостей
 ____

- Приведение типов. В таблице 1 приведены основные типы.
  
- Сохранить датасет в формате (Parquet).

Таблица 1 — Основные типы данных  Pandas, Python и NumPy.

Pandas dtype mapping 

| Pandas dtype | Python type	   |NumPy type	 |     Usage       |
| :---         |     :---:      |          :--- |         :--- |
| object   |str or mixed     | string_, unicode_, mixed types    |Text or mixed numeric and non-numeric values              |
| int64     | int       |int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64      |Integer numbers              |
| float64     | float       | float_, float16, float32, float64      |	Floating point numbers              |
| bool     | bool       |bool_      |	True/False values              |
| datetime64     | NA       | datetime64[ns]      |Date and time values              |
| timedelta[ns]     | NA       | NA      |Differences between two datetimes              |
| category     | NA       | NA      |	Finite list of text values              |

 **Apache Parquet** — формат хранения данных с открытым исходным кодом, ориентированный на столбцы. В отличие от строковых форматов (например, CSV или JSON), где данные хранятся построчно, Parquet организует их колонками.

 Вывод данных на рис.3. Сохраяем наш датасет в формате [Parquet](https://github.com/Staruslan/data-engineering-2025/blob/main/raw_data.parquet)
 
____


