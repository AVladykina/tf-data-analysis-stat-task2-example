import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 433242632 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
 # Вычисляем оценки параметров
    loc = x.mean() - 0.056 / 2
    scale = np.sqrt(12) * (x.std() + 0.056 / 2) / np.sqrt(len(x))
    
    # Вычисляем доверительный интервал
    alpha = 1 - p
    left = loc - scale * norm.ppf(1 - alpha / 2)
    right = loc + scale * norm.ppf(1 - alpha / 2)
    
    return left, right
