import pandas as pd
import numpy as np

class ExecutionEvaluator:
    def __init__(self, benchmark_col='wap_mean'):
        self.benchmark_col = benchmark_col

    def get_diagnostics(self, df, action_label='Dip Snipe (Aggressive)'):
        """
        Calculates institutional-grade execution metrics.
        """
        results = {}
        
        #IS
        market_avg = df[self.benchmark_col].mean()
        executed_trades = df[df['action'] == action_label]
        
        if not executed_trades.empty:
            exec_avg = executed_trades[self.benchmark_col].mean()
            is_bps = ((exec_avg - market_avg) / market_avg) * 10000
            results['is_bps'] = is_bps
        else:
            results['is_bps'] = 0

        #hit ratio (assumes each row is 1s of data)
        df['future_price_30s'] = df[self.benchmark_col].shift(-30)
        executed_trades = df[df['action'] == action_label].copy()
        
        if not executed_trades.empty:
            hit_mask = executed_trades['future_price_30s'] > executed_trades[self.benchmark_col]
            results['hit_ratio'] = hit_mask.mean()
        else:
            results['hit_ratio'] = 0

        results['switch_ratio'] = (df['regime'] != df['regime'].shift(1)).mean()
        
        return results