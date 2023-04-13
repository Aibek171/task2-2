import pandas as pd
import numpy as np


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.01
    stat, p_value = ks_2samp(x, y)
    if p_value < alpha:
        return True
    else:
        return False
