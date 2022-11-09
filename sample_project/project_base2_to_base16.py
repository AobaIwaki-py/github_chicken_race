from converter_base10_to_base16 import converter_base10_to_base16
from converter_base2_to_base10 import base10_converter
from create_binary import base2_create
from separator import base2_separator
"""
16桁の2進数を4桁刻みにして10進数に変換し、変換した10進数をさらに16進数に変換する
プログラムを制作するプロジェクト
"""
if __name__ == "__main__":
        # 16桁の2進数の生成
        base2_list = base2_create()
        print('生成された2進数', base2_list)
        # 動作確認
        # print(  base2_list, 
        #         base2_list.shape, 
        #         type(base2_list))
        # 2進数を4つずつに区切る
        base2_list = base2_separator(base2_list)
        # 動作確認
        # print(  base2_list, 
        #         base2_list.shape,
        #         type(base2_list))
        # 区切られた2進数を10進数に変換する
        base10_list = base10_converter(base2_list)
        # 動作確認
        # print(  base10_list,
        #         base10_list.shape,
        #         type(base10_list),
        #         type(base10_list[0]))
        # 10進数を16進数に変換する
        base16_number = converter_base10_to_base16(base10_list)
        # 動作確認
        # print(  base16_number,
        #         type(base16_number))
        print('処理後の16進数', base16_number)

