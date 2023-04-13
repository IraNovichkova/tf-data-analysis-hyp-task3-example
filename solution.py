import pandas as pd
import numpy as np
from scipy import stats


chat_id = 335933917 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p = 0.09
    if (stats.ttest_ind(x, y).pvalue > p):
        return True
    else:
        return False
