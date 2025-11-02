import os
import pandas as pd
from sqlalchemy import create_engine, inspect, text

# from dotenv import load_dotenv


def create_engine_and_inspector():
    load_dotenv()
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_url = os.getenv("DB_URL")
    db_port = os.getenv("DB_PORT")
    db_name = "homeworks"

    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"
    )

    inspector = inspect(engine)
    return engine, inspector


def save_to_parquet(df, parquet_path="data/processed/output.parquet"):
    df.to_parquet(parquet_path, engine="pyarrow", index=False)
    print(f"Data saved to Parquet at {parquet_path}")


def load_data_to_postgres(df, engine):
    table_name = "komarov"
    with engine.connect() as conn:
        print("Successfully connected to PostgreSQL")

    df.to_sql(
        name=table_name,
        con=engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data loaded into PostgreSQL table: {table_name}")

    with engine.begin() as conn:
        conn.execute(text(f"ALTER TABLE public.{table_name} ADD PRIMARY KEY (index)"))


def print_table_structure(inspector, table_name="komarov"):
    columns = inspector.get_columns(table_name, schema="public")
    print("\nTable structure:")
    print({col["name"]: col["type"] for col in columns})


def load(df: pd.DataFrame, parquet_path: str = "data/processed/output.parquet"):
    """Load data to PostgresSQL and save as Parquet."""
    save_to_parquet(df, parquet_path)
    engine, inspector = create_engine_and_inspector()
    load_data_to_postgres(df, engine)
    print_table_structure(inspector)
