### 24. 基本的な関数の定義と呼び出し
print("2つの整数を受け取り、その和を返す関数 `add` を定義してください。その後、関数を使って `3` と `5` の和を表示してください。")

def add (num1, num2):
    return num1 + num2

print(add(3,5))

### 25. 関数の引数と返り値
print("1つの整数を受け取り、その値が偶数か奇数かを判定して文字列 'even' または 'odd' を返す関数 `even_or_odd` を定義してください。その後、関数を使って `4` と `7` の結果を表示してください。")

def even_or_odd (num):
    if num % 2 == 0:
        return "even"
    return "odd"

print(even_or_odd(4))
print(even_or_odd(7))


### 26. 複数の引数
print("3つの文字列を受け取り、それらをスペースで連結して返す関数 `concatenate_strings` を定義してください。その後、関数を使って 'Hello', 'world', '!' を連結した結果を表示してください。")

def concatenate_strings(str1,str2,str3):
    return f"{str1} {str2} {str3}"

print(concatenate_strings("Hello","world","!"))


### 27. デフォルト引数

print("名前を受け取って 'Hello, [名前]!' というメッセージを返す関数 `greet` を定義してください。名前が指定されない場合は 'Hello, Guest!' というメッセージを返すようにしてください。その後、関数を使って 'Alice' と名前が指定されていない場合の結果を表示してください。")

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())

