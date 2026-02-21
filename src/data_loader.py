import pandas as pd
import os

def load_book_data(file_path: str) -> pd.DataFrame:
    """
    Loads Limit Order Book parquet files.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
    
    df = pd.read_parquet(file_path)
    
    df.sort_values(by=['time_id', 'seconds_in_bucket'], inplace=True)
    return df

