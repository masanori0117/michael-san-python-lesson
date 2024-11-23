### 38. 三項演算子１
print('1. ランダムに生成された整数を持つ変数を宣言し、その変数の値が偶数であれば "even"、奇数であれば "odd" と出力するプログラムを、三項演算子を使って作成してください。')
import random
number = random.randint(1,100)
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}.")
print("")


### 39. 標準入力
print("次の仕様に従って、ユーザーの名前と年齢を入力し、最終的なメッセージを出力するプログラムを作成してください。")

def check_name(name):
    # 名前が空または  Noneの場合はエラーメッセージを表示
    if name == "" or name is None:
        print("名前を入力してください")
        return False
    # 名前が10文字以上の場合はエラーメッセージを表示
    elif len(name) > 10:
        print("名前は10文字以内で入力してください")
        return False
    # それ以外は名前は有効
    else:
        return True

def check_age(age):
    # 年齢が空の場合エラーを表示
    if age == "" or age is None:
        print("年齢を入力してください")
        return False
    # 数字が入力されていない場合&0歳以上でない場合はエラーを表示
    if age.isdigit():
        age = int(age)
        if age >= 0:
            return True
        else:
            print("年齢は0以上の正の数字を入力してください")
            return False
    else:
        print("年齢は数字を入力してください")
        return False

def input_process(prompt, check_func):
    # 入力を求めるメッセージを表示
    value = input(prompt)
    # バリデーション関数を呼び出してチェック
    if check_func(value):
        return value
    else:
        # 無効な場合、再入力を求める
        return input_process(prompt, check_func)

def desplay_message(name, age):
    # 入力された情報を出力
    print(f"{name}さん（年齢: {age}歳）、ご登録ありがとうございます！")


def main():
    name = input_process("あなたの名前を入力してください", check_name)
    age = input_process(f"{name}さん、あなたの年齢は何歳ですか？", check_age)
    desplay_message(name, age)

# main関数を呼び出し
if __name__ == "__main__":
    main()