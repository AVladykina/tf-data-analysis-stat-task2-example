import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 433242632 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    a = 0.056  # левая граница равномерного распределения
    b = np.max(x)  # правая граница равномерного распределения
    delta = (b - a) * np.sqrt(1 - p) / 2
    return a + delta, b - delta
#     alpha = 1 - p
#     loc = x.mean()
#     scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)
