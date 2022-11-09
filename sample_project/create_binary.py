# 出力：16桁の二進数をランダムで作るndarray
# 仕様：
import numpy as np

def base2_create(a=0,b=2,c=16):
    binary_array = np.random.randint(a,b, (c))
    return binary_array

if __name__ == "__main__":
    print(base2_create())
    print(type(base2_create()))
