# 1. 基本的な変数の宣言
# 以下の指定された条件に合うような値を変数に代入# して宣言してください。
# また宣言した変数を出力してください。

number = 5
text = "test"
flag = True
test = None
pi = 3.14

print(number)
print(text)
print(flag)
print(test)
print(pi)

# 2. 基本的な計算
# 整数型の2つの変数を宣言してください。2つの変数を用いて、足す、引く、かける、割る、割った余りを出力してください。

num1 = 5
num2 = 2

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
divion = num1 / num2
modulo = num1 % num2

print(addition)
print(subtraction)
print(multiplication)
print(divion)
print(modulo)


# 3. 条件式と論理型（boolean）について
# 初期値がFalseである論理型の変数を宣言してください。問題2で宣言した2つの変数を足した結果が偶数であれば、論理型の変数にTrueを代入してください。

is_even = False

if addition %2 == 0:
    is_even = True
print(is_even)


# 4. 条件式
# 設問3のboolean型の変数を利用した条件式を作成し、以下のように出力してください。

# 偶数なら「偶数です」
# 奇数なら「奇数です」

if is_even == True:
    print("偶数です")
else:
    print("奇数です")
