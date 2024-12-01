### 38. 三項演算子１
print('1. ランダムに生成された整数を持つ変数を宣言し、その変数の値が偶数であれば "even"、奇数であれば "odd" と出力するプログラムを、三項演算子を使って作成してください。')
import random
number = random.randint(1,100)
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}.")
print("")


### 39. 標準入力
print("次の仕様に従って、ユーザーの名前と年齢を入力し、最終的なメッセージを出力するプログラムを作成してください。")

def input_process(input_type, name=None):
    """
    名前と年齢を入力してもらい、バリデーションを行い、入力した内容に値が問題なければ値を返し、問題があればエラーメッセージを表示して再入力を促します
    :Args
        input_type (str): 入力の種類 ("name" または "age")
        name (str): 名前
    :Return
        Boolean: nameもしくはageを返す or 再帰関数でinput_processを再実行
    """
    # 名前のバリデーション関数
    def check_name(name):
        """名前のバリデーションを行います"""
    # 名前が空または  Noneの場合はエラーメッセージを表示
        if name == "" or name is None:
            print("名前を入力してください")
            return False
        # 名前が10文字以上の場合はエラーメッセージを表示
        if len(name) > 10:
            print("名前は10文字以内で入力してください")
            return False
        # それ以外は名前は有効
        return True

    # 年齢のバリデーション関数
    def check_age(age):
        """年齢のバリデーションを行います"""
        # 年齢が空の場合エラーを表示
        if age == "" or age is None:
            print("年齢を入力してください")
            return False
        # 数字が入力されていない場合&0歳以上でない場合はエラーを表示
        if age.isdigit():
            age = int(age)
            # 年齢が0歳以上のバリデーション
            if age >= 0:
                return True
            print("年齢は0以上の正の数字を入力してください")
            return False
        # 数字が入力されているかの確認
        print("年齢は数字を入力してください")
        return False

    # 名前入力を求めるメッセージとバリデーション関数の呼び出し
    if input_type == "name":
        name = input("あなたの名前を入力してください")
        if check_name(name):
            return name
        # 無効な場合、再入力を求める
        return input_process("name")
    # 年齢入力を求めるメッセージとバリデーション関数の呼び出し
    if input_type == "age":
        age = input(f"{name}さん、あなたの年齢は何歳ですか？")
        if check_age(age):
            return int(age)
        # 無効な場合、再入力を求める
        return input_process("age", name)


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