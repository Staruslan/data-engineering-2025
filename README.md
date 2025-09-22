# **Data Engineering (Project 2025)**

**Студент ПИШ ИТМО**: Комаров Руслан

**Преподаватель:** Пандаков Виктор Викторович
 ____

 :white_check_mark: (ДЗ1) 
 
 - Ссылка на датасет: https://drive.google.com/drive/folders/17CqpL_vUcgqztIK5kGpLKhGqC8Ex8KJ-?usp=drive_link 

 - Данные для исследования, запись передвижения биологического объекта (лабораторная мышь) приведена на рис.1.
<img width="329" height="430" alt="image" src="https://github.com/user-attachments/assets/1f542dbc-c7a1-47f5-954d-73e61a89efba" />
   
Рисунок 1 — Лабораторная мышь при проведении теста
 ____
:white_check_mark: (ДЗ2)

- Скрипт [data_loader.py](https://github.com/Staruslan/data-engineering-2025/blob/main/data_loader.py) на Python для чтения датасета.
Данный скрипт работает в связке [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)+[poetry](https://python-poetry.org/docs/basic-usage/). 


- Вывод файла зависимостей [pyproject.toml](https://github.com/Staruslan/data-engineering-2025/blob/main/pyproject.toml);

- Вывод первых 10 строк из наших данных на рис.2.

<img width="1915" height="660" alt="DL_Result" src="https://github.com/user-attachments/assets/c13ed3d4-ef54-48a0-abe5-a72f1c5fa44d" />


Рисунок 2 — Вывод первых 10 строк из наших данных

____

:black_square_button: (ДЗ3)

Сохранить датасет в формате (Parquet)

- **Apache Parquet** — формат хранения данных с открытым исходным кодом, ориентированный на столбцы. В отличие от строковых форматов (например, CSV или JSON), где данные хранятся построчно, Parquet организует их колонками.
____

:black_square_button: (ДЗ4)
