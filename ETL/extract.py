import pandas as pd
import requests
from io import StringIO
import os
from .validate import validate_raw_data

def extract_data(url: str, raw_data_path: str) -> pd.DataFrame:
    """
    Extract data from Google Drive and save as CSV
    """
    print("Starting data extraction...")
    
    file_id = url.split('/')[-2]
    dwn_url = f'https://drive.google.com/uc?export=download&id={file_id}'
    url2 = requests.get(dwn_url).text
    csv_raw = StringIO(url2)
    raw_data = pd.read_csv(csv_raw)
    
    # Validate raw data
    validate_raw_data(raw_data)
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)
    
    # Save raw data
    raw_data.to_csv(raw_data_path, index=False)
    print(f'Raw data successfully saved: {raw_data_path}')
    
    return raw_data
