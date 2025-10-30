import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Apply types and check for null values."""
    types_dict = {
        'bodyparts': 'int64',
        'snout_x': 'float64', 'snout_y': 'float64', 'likelihood': 'float64',
        'leftforword_x': 'float64', 'leftforword_y': 'float64', 'likelihood.1': 'float64',
        'rightforword_x': 'float64', 'rightforword_y': 'float64', 'likelihood.2': 'float64',
        'midbody_x': 'float64', 'midbody_y': 'float64', 'likelihood.3': 'float64',
        'leftback_x': 'float64', 'leftback_y': 'float64', 'likelihood.4': 'float64',
        'rightback_x': 'float64', 'rightback_y': 'float64', 'likelihood.5': 'float64',
        'tail_x': 'float64', 'tail_y': 'float64', 'likelihood.6': 'float64'
    }

    for col, dtype in types_dict.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)
        else:
            print(f"Warning: Column {col} not found in DataFrame")

    null_counts = df.isnull().sum()
    print("Null values in each column:")
    print(null_counts[null_counts > 0] if null_counts.sum() > 0 else "No nulls found")

    df.to_csv('data/transform/transform_data.csv')
