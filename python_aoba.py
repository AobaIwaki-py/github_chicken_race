# お願い
# 関数addの引数を三つにして3つの数の足し算ができるようにしてほしい
# 型ヒントをfloatに変えて欲しい

# 計算用プログラム
# 足し算
def add(a: float, b: float, c:float) -> float:
    return (a + b + c)

# 実行
if __name__ == "__main__":
    print(add(2,3,4))
