### 38. 三項演算子１
print('1. ランダムに生成された整数を持つ変数を宣言し、その変数の値が偶数であれば "even"、奇数であれば "odd" と出力するプログラムを、三項演算子を使って作成してください。')
import random
number = random.randint(1,100)
result = "even" if number %2 == 0 else "odd"
print(f"{number} is {result}.")
print("")


### 39. 標準入力
print("次の仕様に従って、ユーザーの名前と年齢を入力し、最終的なメッセージを出力するプログラムを作成してください。")

name = input("あなたの名前を教えてください。")
age = input(f"{name}さん、あなたの年齢は何歳ですか？")
print(f"{name}さん（年齢:{age}）、ご登録ありがとうございます！")
