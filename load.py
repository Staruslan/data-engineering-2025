import pandas as pd

def load(df: pd.DataFrame, parquet_path: str = "data/processed/output.parquet"):
    """Load data to PostgresSQL and save as Parquet."""
    df.to_parquet(parquet_path, engine='pyarrow', index=False)
    print(f"Data saved to Parquet at {parquet_path}")

    load_dotenv()
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_url = os.getenv('DB_URL')
    db_port = os.getenv('DB_PORT')
    db_name = "homeworks"
    table_name = "komarov"

    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"
    )
    with engine.connect() as conn:
        print("Successfully connected to PostgreSQL")

    df.to_sql(
        name=table_name,
        con=engine,
        schema="public",
        if_exists="replace",
        index=True
    )
    print(f"Data loaded into PostgreSQL table: {table_name}")

    with engine.begin() as conn:
        conn.execute(text(f'ALTER TABLE public.{table_name} ADD PRIMARY KEY (index)'))

    inspector = inspect(engine)
    columns = inspector.get_columns(table_name, schema="public")
    print("\nTable structure:")
    print({col["name"]: col["type"] for col in columns})
