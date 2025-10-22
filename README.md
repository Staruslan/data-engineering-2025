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
 
 <img width="787" height="567" alt="image" src="https://github.com/user-attachments/assets/23f5290a-b15e-4f4a-be29-9737d2018341" />
 
Рисунок 3 - Вывод данных

# EDA для DE

> [!NOTE]
> EDA - разведочный анализ данных
> 
> EDA - это процесс изучения данных с
целью раскрытия их скрытых
закономерностей, выявления важных
характеристик и понимания взаимосвязей
между переменными

В моем [Notebook](https://github.com/Staruslan/data-engineering-2025/blob/main/data_loader.py](https://github.com/Staruslan/data-engineering-2025/blob/main/Notebook/EDA.py))  отсутствуют следующие элементы: названия, временные метки и количественные величины. Данный набор данных содержит записи о передвижении лабораторной мыши, которые фиксируют ее перемещения без указания конкретных названий объектов или временных интервалов.

Я в этом проекте использовал четыре метрики:

1. Completeness - Полнота данных;
2. Uniqueness - Уникальность записей;
3. Duplication Rate – уровень дубликатов;
4. Accuracy – точность данных.

**1. Completeness (Полнота данных):** 

Эта метрика показывает, какая доля данных не содержит пропущенных значений. Значение близкое к 100% указывает на высокую полноту данных.

**2. Uniqueness (Уникальность записей):**

Эта метрика измеряет долю уникальных записей в наборе данных. Высокое значение говорит о том, что данные не содержат много дубликатов.

**3. Duplication Rate (Уровень дубликатов):** 

Это обратная метрика к уникальности и показывает долю дубликатов в наборе данных.

**4. Accuracy (Точность данных):** 

Эта метрика требует понимания того, какие значения в ваших данных считаются правильными или допустимыми. Это может потребовать дополнительного анализа и определения правил для оценки точности.

**Оценка качества данных** 

<img width="1720" height="745" alt="image" src="https://github.com/user-attachments/assets/6c48f67f-4f53-4643-8cca-29c42e23d858" />

<img width="907" height="763" alt="image" src="https://github.com/user-attachments/assets/b515969a-048a-4a53-b97a-80a5bd56e638" />

# Работа с базой данных

> [!NOTE]
> **База данных** — это организованная совокупность данных, хранимая вместе со структурой (связи,
ограничения, правила целостности и проч.), обеспечивающее эффективный доступ, изменение и
управление этими данными.

<img width="662" height="312" alt="image" src="https://github.com/user-attachments/assets/80ac76ae-ceb3-421a-96a3-5ab71e855463" />
<img width="550" height="255" alt="image" src="https://github.com/user-attachments/assets/9ea5072d-893d-4801-bb85-622f31b908e1" />

В этой части проекта требовалось найти таблицу доступа в базе данных формата SQLite (.db). После этого, используя полученные учетные данные, осуществлялось подключение к удаленной базе данных PostgreSQL, как описано в файле [write_to_db.py](write_to_db.py). Затем в удаленную базу загружались 100 строк выбранного в проекте набора данных.


# Работа с визуализацией
> [!NOTE]
> **Все роли Data Science создают визуализации, но при этом преследуют разные цели.**
>
> Целевая аудитория моего проекта — исследователи в области медицины, которые смогут использовать эти данные для реконструкции траекторий движения.





