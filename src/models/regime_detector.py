from hmmlearn import hmm
import numpy as np

import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM

class MarketRegimeModel:
    def __init__(self, n_components=2, random_state=42):
        self.n_components = n_components
        self.model = GaussianHMM(
            n_components=self.n_components, 
            covariance_type="full", 
            n_iter=100, 
            random_state=random_state
        )
        self.crash_state = None

    def fit_predict(self, df_features: pd.DataFrame, feature_cols: list) -> np.ndarray:
        """
        Fits the HMM to the microstructure features and returns the hidden states.
        Automatically identifies the high slippage state based on the variance of the spread.
        """
        X = df_features[feature_cols].values
        self.model.fit(X)
        states = self.model.predict(X)
        
        #identify crash state, regime with the highest variance in the bid ask spread (featrue 0) is flagged.
        variances = []
        for i in range(self.n_components):
            state_mask = (states == i)
            if np.sum(state_mask) > 0:
                variances.append(np.var(X[state_mask, 0])) 
            else:
                variances.append(0)
                
        self.crash_state = np.argmax(variances)
        return states

    def predict(self, current_features: np.ndarray) -> np.ndarray:
        """Predicts the regime for live, incoming tick data."""
        return self.model.predict(current_features)
        
    def is_crash_regime(self, state: int) -> bool:
        return state == self.crash_state