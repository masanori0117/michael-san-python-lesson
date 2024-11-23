### 38. 三項演算子１
print('1. ランダムに生成された整数を持つ変数を宣言し、その変数の値が偶数であれば "even"、奇数であれば "odd" と出力するプログラムを、三項演算子を使って作成してください。')
import random
number = random.randint(1,100)
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}.")
print("")


### 39. 標準入力
print("次の仕様に従って、ユーザーの名前と年齢を入力し、最終的なメッセージを出力するプログラムを作成してください。")

def main():

    def input_name():
        # 名前を入力
        name = input("あなたの名前を教えてください。")

        # 名前のバリデーション
        # 空白と名前の長さ(10文字以下)のバリデーション
        if name == "" or name is None:
            print("名前を入力してください")
            return input_name()

        elif len(name) > 10:
            print("名前は10文字以内で入力してください")
            return input_name()

        else:
            return name

    def input_age():
        # 年齢を入力
        age = input(f"{name}さん、あなたの年齢は何歳ですか？")

        # 年齢のバリデーション
        # 空白のバリデーション
        if age == "" or age is None:
            print("年齢を入力してください")
            return input_age()
        # 数字入力 & 0歳以上かどうかのバリデーション
        if age.isdigit():
            age = int(age)
            if age >= 0:
                return age
            else:
                print("年齢は0以上の正の数字を入力してください")
                return input_age()
        else:
            print("年齢は数字を入力してください")
            return input_age()

    name = input_name()
    age = input_age()

    print(f"{name}さん（年齢:{age}）、ご登録ありがとうございます！")

# main関数を呼び出し
if __name__ == "__main__":
    main()