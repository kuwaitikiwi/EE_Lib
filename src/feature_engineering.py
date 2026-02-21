import pandas as pd
import numpy as np

def wap(df: pd.DataFrame) -> pd.Series:
    wap = (df['bid_price1'] * df['ask_size1'] + df['ask_price1'] * df['bid_size1']) / (
           df['bid_size1'] + df['ask_size1'])
    return wap

def log_return(series: pd.Series) -> pd.Series:
    return np.log(series).diff()

def realized_vol(series: pd.Series) -> float:
    return np.sqrt(np.sum(series**2))

def build_microstructure_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate tick-level LOB data into WAP, Log Returns, Spread, OBI and Realized Vol
    """
    df['wap'] = wap(df)
    df['log_return'] = df.groupby('time_id')['wap'].transform(log_return)
    
    #bid ask spread: wider spread = lower liquidity
    df['spread'] = (df['ask_price1'] - df['bid_price1']) / df['bid_price1']
    
    #order book impalanc positive =  buying pressure, neg = selling pressure
    df['obi'] = (df['bid_size1'] - df['ask_size1']) / (df['bid_size1'] + df['ask_size1'])
    
    feature_dict = {
        'wap': ['mean'],
        'spread': ['mean', 'max'],
        'obi': ['mean', 'std'],
    }
    
    df_agg = df.groupby('time_id').agg(feature_dict)
    df_agg.columns = ['_'.join(col).strip() for col in df_agg.columns.values]
    
    vol_df = df.groupby('time_id')['log_return'].agg(realized_vol).rename('realized_volatility')
    
    return pd.concat([df_agg, vol_df], axis=1).dropna()