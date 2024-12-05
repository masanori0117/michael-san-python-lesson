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
    """名前のバリデーションを行います
    :Args
        name (str): 名前
    """
    if name == "" or name is None:
        print("名前を入力してください")
        return False
    if len(name) > 10:
        print("名前は10文字以内で入力してください")
        return False
    return True

def check_age(age):
    """年齢のバリデーションを行います
    :Args
        age (str): 年齢
    """
    if age == "" or age is None:
        print("年齢を入力してください")
        return False
    if not age.isdigit():
        print("年齢は数字を入力してください")
        return False
    age = int(age)
    if age < 0:
        print("年齢は0以上の正の数字を入力してください")
        return False
    return True

def input_process(input_type, name=None):
    """
    名前と年齢を入力してもらい、バリデーションを行い、入力した内容に値が問題なければ値を返し、問題があればエラーメッセージを表示して再入力を促します
    :Args
        input_type (str): 入力の種類 ("name" または "age")
        name (str): 名前
    :Return
        Boolean: nameもしくはageを返す or 再帰関数でinput_processを再実行
    """

    if input_type == "name":
        prompt = "あなたの名前を入力してください"
    elif input_type == "age":
        prompt = f"{name}さん、あなたの年齢は何歳ですか？"
    else:
        raise ValueError("無効な入力タイプです")

    input_val = input(prompt)

    if input_type == "name" and check_name(input_val):
        return input_val
    elif input_type == "age" and check_age(input_val):
        return input_val
    else:
        return input_process(input_type, name)


def display_message(name, age):
    """入力された名前と年齢を表示します"""
    print(f"{name}さん（年齢: {age}歳）、ご登録ありがとうございます！")

def main():
    name = input_process("name")
    age = input_process("age", name)
    display_message(name, age)

# main関数を呼び出し
if __name__ == "__main__":
    main()