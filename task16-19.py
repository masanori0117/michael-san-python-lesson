### 16. リストの作成とアクセス
print("1. 空のリストを作成し、表示してください。")
nums = []
print(nums)

print("")
print("2. 数字のリスト `[1, 2, 3, 4, 5]` を作成し、リストの最初の要素と最後の要素を表示してください。")
nums = [1, 2, 3, 4, 5]

print(nums)
print(f"最初の要素: {nums[0]}")
print(f"最後の要素: {nums[-1]}")

print("")
### 17. リストの操作
print("1. リスト `[1, 2, 3, 4, 5]` に要素 `6` を追加してください。")
nums.append(6)
print(nums)

print("")

print("2. リスト `[1, 2, 3, 4, 5]` の3番目の要素を `10` に変更してください。")
nums = [1, 2, 3, 4, 5]
nums[2] = 10
print(nums)
print("")


print("3. リスト `[1, 2, 3, 4, 5]` から要素 `3` を削除してください。")
nums = [1, 2, 3, 4, 5]
nums.remove(3)
print(nums)
print("")

print("4. リスト `[1, 2, 3, 4, 5]` を逆順にしてください。")
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)
print("")

### 18. リストの操作（応用）

print("1. リスト `[1, 2, 3, 4, 5]` の要素を全て2倍にするコードを書いてください。")
nums = [1, 2, 3, 4, 5]
nums = [num * 2 for num in nums]
print(nums)

print("")

print("2. リスト `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` から偶数だけを取り出して新しいリストを作成してください。")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print(even_nums)
print("")

print("3. 文字列リスト `['apple', 'banana', 'cherry']` の各要素の長さを表示してください。")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"{fruit}の要素長さ: {len(fruit)} ")
print("")

print("4. リスト `[1, 2, 3, 4, 5]` と `[6, 7, 8, 9, 10]` を結合してください。")
nums = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
sum = nums + nums2
print(sum)
print("")

### 19. リスト内包表記
print("1. リスト `[1, 2, 3, 4, 5]` の各要素を3倍にした新しいリストを作成してください。")
nums = [1, 2, 3, 4, 5]
nums_3times = []

for num in nums:
    num_3times = num * 3
    nums_3times.append(num_3times)
print(nums_3times)
print("")

print("2. リスト `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` から奇数だけを取り出して新しいリストを作成してください。")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_odd = []

for num in nums:
    if num % 2 != 0:
        nums_odd.append(num)
print(nums_odd)
print("")
