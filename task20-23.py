### 20. リストの関数
print("1. リスト `[1, 2, 3, 4, 5]` の最大値、最小値、合計を求めてください")
nums = [1, 2, 3, 4, 5]
max_value = max(nums)
min_value = min(nums)
sum_value = sum(nums)

print(f"最大値: {max_value}")
print(f"最小値: {min_value}")
print(f"合計: {sum_value}")
print("")

print("2. リスト `[1, 2, 3, 4, 5]` の平均値を求めてください")
len_value = len(nums)
ave_value = sum_value / len_value
print(f"平均値:{ave_value}")
print("")

### 21. リストのソート
print("1. リスト `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]` を昇順にソートしてください。")
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nums.sort()
print(nums)
print("")

print("2. リスト `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]` を降順にソートしてください。")
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nums.sort(reverse=True)
print(nums)
print("")

### 22. リストのスライス
print("1. リスト `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` の最初の5つの要素を取り出してください。")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first5_elements = nums[:5]
print(first5_elements)
print("")

print("2. リスト `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` の後ろから3つの要素を取り出してください。")
last3_elements = nums[-3:]
print(last3_elements)
print("")

### 23. 二次元リスト
print("1. 二次元リスト `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` の2行目の全ての要素を表示してください。")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print("")

print("2. 二次元リスト `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` の各行の最初の要素を取り出してリストにしてください。")
first_elements = []
for first_element in matrix:
    first_elements.append(first_element[0])
print(first_elements)
print("")
