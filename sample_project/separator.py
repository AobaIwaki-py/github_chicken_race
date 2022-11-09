# 入力：16桁の2進数がndarrayで入ってくる
# 出力：一つのリストの要素数が4の多次元ndarray
# 仕様：入力された2進数を4桁ごとに区切る
import numpy as np

def base2_separator(base2_list: 'np.ndarray'):
    return base2_list.reshape(4,4)

if __name__ == "__main__":
    sample_list = np.array([0,1,1,0]*4)
    print(base2_separator(sample_list))