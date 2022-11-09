# 入力：10進数を要素にもつndarray
# 出力：16進数のstring
# 仕様：10進数を16進数に変換する
import numpy as np

def converter_base10_to_base16(base10_list: 'np.ndarray'):
    ALPHABET = ["A", "B", "C", "D", "E", "F"]
    base16: str = ""
    for base10 in base10_list:
        if(base10/10 < 1):
            base16 += str(int(base10))
        else:
            base16 += ALPHABET[int(base10%10)]
    return base16
    pass

if __name__ == "__main__":
    sample_list = np.arange(1,16)
    print(sample_list)
    print(converter_base10_to_base16(sample_list))