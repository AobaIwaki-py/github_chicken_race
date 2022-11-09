# 入力：4つに区切られた二進数（ndarray）
# 出力：10進数のndarray
# 仕様：入力で入ってきた4つごとの値を10進数に変換する
import numpy as np


def base10_converter(base2_sep):
    shape = np.shape(base2_sep)
    base10_list = np.zeros(shape[0])

    for index in range(0,4):

        n = 0

        for binary in base2_sep[index,:]:
            
            if(binary == 1):    
                base10_list[index] += 2**(3-n) 

            n += 1  

    return base10_list


if __name__ == "__main__":
    sample_list = np.array([[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0]])
    base10 = base10_converter(sample_list)
    print(base10)
    print(type(base10))

