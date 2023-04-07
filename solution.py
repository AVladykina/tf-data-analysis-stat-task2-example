import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import uniform


chat_id = 433242632 # Ваш chat ID, не меняйте название переменной



def solution(p: float, x: np.ndarray) -> tuple:
    b = np.max(x)
    interval_left = x[-1] + (1-alpha)*(x[-1]-0.056)
    interval_right = b + (1-alpha)*(b-0.056)
    return (interval_left, interval_right)
         
 # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
#     alpha = 1 - p
#     loc = x.mean()
#     scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)
