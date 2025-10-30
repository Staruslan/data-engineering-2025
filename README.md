<h1 align="center">Данные для исследования, запись передвижения биологического объекта.</h1>
   
<p align="center">
  <b>Data Engineering (Project 2025)</b>
</p>


**_Студент ПИШ ИТМО_**: Комаров Руслан

**_Преподаватель_:** Пандаков Виктор Викторович
 ____

 
Запись передвижения биологического объекта (лабораторная мышь) приведена на рис.1.

- Ссылка на датасет: https://drive.google.com/drive/folders/17CqpL_vUcgqztIK5kGpLKhGqC8Ex8KJ-?usp=drive_link
  
<p align="center"><img width="325" height="441" alt="image" src="https://github.com/user-attachments/assets/00d1d28e-0823-4e8e-9826-6977b9f85db0" /></p>

<p align="center">
Рисунок 1 - Лабораторная мышь при проведении теста
</p>


- Скрипт [data_loader.py](https://github.com/Staruslan/data-engineering-2025/blob/main/data_loader.py) на Python для чтения датасета.
Данный скрипт работает в связке [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)+[poetry](https://python-poetry.org/docs/basic-usage/).


1. Создание и активация окружения conda
```
 conda create -n my_env python=3.13 pip
```
```
 conda activate my_env
```
2. Установка Poetry
```
 pip install poetry
```
3. Создание нового проекта с Poetry
```
 poetry new my_project
```
```
 cd my_project
```
4. Добавление зависимостей
```
 poetry add jupyterlab pandas matplotlib wget
```

- Вывод файла зависимостей [pyproject.toml](https://github.com/Staruslan/data-engineering-2025/blob/main/pyproject.toml);

- Вывод первых 10 строк из наших данных на рис.2.

<p align="center">
<img width="1915" height="660" alt="image" src="https://github.com/user-attachments/assets/f4fde124-de16-4bb8-b0a7-c7feaafd040c" />
</p>
<p align="center">
Рисунок 2 - Вывод зависимостей
</p>

- Приведение типов. В таблице 1 приведены основные типы.
  
- Сохранить датасет в формате (Parquet).

Таблица 1 — Основные типы данных  Pandas, Python и NumPy.

**Pandas dtype mapping**

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
 
 <p align="center">
 <img width="787" height="567" alt="image" src="https://github.com/user-attachments/assets/23f5290a-b15e-4f4a-be29-9737d2018341" />
</p>
<p align="center">
Рисунок 3 - Вывод данных
</p>

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

Оценка качества данных приведена на рис.4 

 <p align="center">
<img width="1720" height="745" alt="image" src="https://github.com/user-attachments/assets/6c48f67f-4f53-4643-8cca-29c42e23d858" />
<img width="907" height="763" alt="image" src="https://github.com/user-attachments/assets/b515969a-048a-4a53-b97a-80a5bd56e638" />
</p>
<p align="center">
Рисунок 4 - Качество данных
</p>

# Подключение к БД и считывание из нее учетных данных для подключения к БД PostgreSQL

> [!NOTE]
> **База данных** — это организованная совокупность данных, хранимая вместе со структурой (связи,
ограничения, правила целостности и проч.), обеспечивающее эффективный доступ, изменение и
управление этими данными.

<p align="center">
<img width="662" height="312" alt="image" src="https://github.com/user-attachments/assets/80ac76ae-ceb3-421a-96a3-5ab71e855463" />
<img width="550" height="255" alt="image" src="https://github.com/user-attachments/assets/9ea5072d-893d-4801-bb85-622f31b908e1" />

</p>

Успешный вывод данных приведен на рис.5

 <p align="center">
<img width="1030" height="87" alt="image" src="https://github.com/user-attachments/assets/e5f5334f-3202-453b-b1b9-a5cf9ba3b306" />
<img width="544" height="537" alt="image" src="https://github.com/user-attachments/assets/bdb4c57a-5e76-43a5-98ef-9c34cf0dd5c6" />
</p>
<p align="center">
Рисунок 5 -Вывод данных
</p>


В этой части проекта требовалось найти таблицу доступа в базе данных формата SQLite (.db). После этого, используя полученные учетные данные, осуществлялось подключение к удаленной базе данных PostgreSQL, как описано в файле [write_to_db.py](write_to_db.py). 


# Работа с визуализацией
> [!NOTE]
> Все роли Data Science создают визуализации, но при этом преследуют разные цели.
> 
> В нашем виртуальном окружении должна быть установлена зависимость _plotly_. 

Целевая аудитория моего проекта —  специалисты, занимающиеся изучением поведения лабораторныхкрыс и мониторингом их передвижения в рамках научных исследований в области медицины, которые смогут использовать эти данные для реконструкции траекторий движения.

Данная часть проекта подразумевает работу с визуализацией в нашем файле EDA.ipynb.

 Библиотека plotly имеет в себе элементы JavaScript, то Github не пропускает и не отображает корректно графики. Сделано это в целях безопасности.
 
Полная версия EDA с рабочими графиками _plotly_ представлено в файле [html](https://github.com/Staruslan/data-engineering-2025/blob/main/data_quality_dashboard.html).

# Собираем ETL

> [!NOTE]
> ETL (Extract, Transform, Load) — процесс, с помощью которого данные из разных источников приводят к единому виду и собирают в одном месте.


```

laboratory rat-DE_project/
|
|   ├──etl/
│      ├── __init__.py
│      ├── extract.py     # Extract from GDrive, download data from .xlsx file
│      ├── load.py        # Saved data in .parquet, read data from .parquet and download data in  
│      |                   PostgreSQL
│      ├── main.py        # The entry point to the ETL process
|      └──transform.py   # Cleaning data and conversation types

```
