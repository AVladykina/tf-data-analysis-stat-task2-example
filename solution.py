import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import uniform


chat_id = 433242632 # Ваш chat ID, не меняйте название переменной



def solution(p: float, x: np.ndarray) -> tuple:
    mean = np.mean(x)
    std = np.sqrt(((np.max(x) - 0.056)**2)/12)/np.sqrt(len(x))
    t_value = scipy.stats.t.ppf(1 - p/2, len(x)-1)
    lower = (0.056 + np.max(x))/2 - t_value*std
    upper = (0.056 + np.max(x))/2 + t_value*std
    return (lower, upper)
         
 # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
#     alpha = 1 - p
#     loc = x.mean()
#     scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)
