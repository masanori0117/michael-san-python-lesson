### 28. キーワード引数
print("幅と高さを受け取り、長方形の面積を計算して返す関数 `calculate_area` を定義してください。関数呼び出し時にキーワード引数を使って幅 `5`、高さ `10` で計算した結果を表示してください。")
def calculate_area(width, height):
    return width * height

print(calculate_area(width=5, height=10))
print("")

### 29. 可変長引数
print("複数の整数を受け取り、それらの合計を返す関数 `sum_all` を定義してください。その後、関数を使って `1, 2, 3, 4, 5` の合計を表示してください。")
def sum_all(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5
print(sum_all(1, 2, 3, 4, 5))
print("")


### 30. タプルの作成とアクセス
print("タプル `(1, 2, 3, 4, 5)` を作成し、タプルの最初の要素と最後の要素を表示してください。")
nums = (1, 2, 3, 4, 5)
print(nums[0])
print(nums[-1])
print("")


### 31. タプルの要素の確認
print("タプル `(10, 20, 30, 40, 50)` に `30` が含まれているかどうかを確認するコードを書いてください。")
nums = (10, 20, 30, 40, 50)
if 30 in nums:
    print("True")
else:
    print("false")