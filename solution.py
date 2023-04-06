import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import uniform


chat_id = 433242632 # Ваш chat ID, не меняйте название переменной



def solution(p: float, x: np.ndarray) -> tuple:
    alpha = 1 - p
    loc = np.min(x) + (np.max(x) - np.min(x)) / 2  
    scale = (np.max(x) - np.min(x)) / np.sqrt(12) 
    return loc - scale * uniform.ppf(1 - alpha / 2), \
           loc - scale * uniform.ppf(alpha / 2)
