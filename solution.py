import pandas as pd
import numpy as np
from scipy.stats import cramervonmises_2samp

chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.01
    res = cramervonmises_2samp(x, y)
    if res.pvalue < alpha:
        return True
    else:
        return False
