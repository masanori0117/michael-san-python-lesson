### 32. タプルの結合
print("1. タプル `(1, 2, 3)` と `(4, 5, 6)` を結合し、新しいタプルを作成してください。")
nums_tuple1 = (1, 2, 3)
nums_tuple2 = (4, 5, 6)
added_nums_tuple = nums_tuple1 + nums_tuple2
print(added_nums_tuple)
print("")

### 33. タプルのスライス
print("1. タプル `(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)` の最初の5つの要素と、後ろから3つの要素を表示してください。")
nums_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(nums_tuple[:5])
print(nums_tuple[-3:])
print("")

### 34. タプルのアンパッキング
print('1. タプル `("Alice", 24, "Engineer")` をそれぞれ名前、年齢、職業にアンパックし、個別に表示してください。')
person = ("Alice", 24, "Engineer")
name, age, job = person
print(f"名前: {name}")
print(f"年齢: {age}")
print(f"職業: {job}")
print("")


### 35. ネストされたタプル
print("1. タプル `((1, 2), (3, 4), (5, 6))` の要素 `(3, 4)` の2番目の要素を表示してください。")
nums = ((1, 2), (3, 4), (5, 6))
print(nums[1][1])
print("")


### 36. タプルからリストへの変換
print("1. タプル `(1, 2, 3, 4, 5)` をリストに変換し、逆順にして表示してください。")
nums_tuple = (1, 2, 3, 4, 5)
nums = list(nums_tuple)
nums.reverse()
print(nums)
print("")

### 37. リストからタプルへの変換
print("1. リスト `[10, 20, 30, 40, 50]` をタプルに変換し、表示してください。")
nums = [10, 20, 30, 40, 50]
nums_tuple = tuple(nums)
print(nums_tuple)
print("")

