import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import uniform


chat_id = 433242632 # Ваш chat ID, не меняйте название переменной



def solution(p: float, x: np.ndarray) -> tuple:
lower_bound = np.min(x)
loc = lower_bound + (1 - p) * (np.max(x) - lower_bound)
scale = (np.max(x) - lower_bound) / np.sqrt(12)
return loc - scale, loc + scale
