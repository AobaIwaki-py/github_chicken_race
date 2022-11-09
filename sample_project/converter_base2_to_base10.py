# 入力：4つに区切られた二進数（ndarray）
# 出力：4つの値ごとに10進数に変換（ndarray）
# 仕様：入力、出力ともにndarray型
import numpy as np

def base2_create(a=0,b=2,c=16):
    binary_array = np.random.randint(a,b, (c))
    return binary_array

if __name__ == "__main__":
    print(base2_create())
    print(type(base2_create()))