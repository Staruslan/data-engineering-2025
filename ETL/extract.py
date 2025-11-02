import pandas as pd
import requests
from io import StringIO
import os


def extract(url: str, save_path: str = "data/raw/raw_data.csv") -> pd.DataFrame:
    """Download file from Google Drive and save as CSV."""
    file_id = url.split("/")[-2]
    dwn_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(dwn_url).text
    csv_raw = StringIO(response)
    df = pd.read_csv(csv_raw)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"Data extracted and saved to {save_path}")
    return df
