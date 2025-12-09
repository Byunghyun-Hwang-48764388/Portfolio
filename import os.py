import os
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import warnings
import kaggle_evaluation.default_inference_server

# read CSV 
train = pd.read_csv("train.csv")

# NaN, Inf 제거
train = train.fillna(0).replace([np.inf, -np.inf], 0)

# 확실히 float 타입으로 변환
train = train.astype(float)

# forward_returns가 거의 상수인 행 제거 (std가 0이면 SVD 문제 가능)
train = train.loc[train["forward_returns"].rolling(2).std().fillna(0) > 1e-8]

# risk_free_rate도 안정화
train["risk_free_rate"] = train["risk_free_rate"].clip(-1e3, 1e3)


