import os
import pandas as pd
from etl import extract, transform, load
if __name__ == "__main__":
    url='https://drive.google.com/file/d/1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq/view?usp=share_link'

    choice = input("What do you want to do? [extract/transform/load]: ").strip().lower()

    if choice == "extract":
        df = extract(url)
    elif choice == "transform":
        # Assume CSV already exists locally
        csv_path = "data/raw/raw_data.csv"
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            os.makedirs(os.path.dirname('data/transform/'), exist_ok=True)
            transform(df)
            print('Data was transformed')
        else:
            print(f"{csv_path} not found. Please run extract first.")
    elif choice == "load":
        csv_path = 'data/transform/transform_data.csv'
        if os.path.exists(csv_path):
            load(pd.read_csv(csv_path))
        else:
            print(f"Transformed dataframe was not found. Please run transform first.")
    else:
        print("Invalid choice. Please select 'extract', 'transform', or 'load'.")
