### 16. リストの作成とアクセス
print("1. 空のリストを作成し、表示してください。")
list1 = []
print(list1)

print("")
print("2. 数字のリスト `[1, 2, 3, 4, 5]` を作成し、リストの最初の要素と最後の要素を表示してください。")
list2 = [1,2,3,4,5]
print(list2[0])
print(list2[-1])

print("")
### 17. リストの操作
print("1. リスト `[1, 2, 3, 4, 5]` に要素 `6` を追加してください。")
list2.append(6)
print(list2)

print("")

print("2. リスト `[1, 2, 3, 4, 5]` の3番目の要素を `10` に変更してください。")
list3 = [1, 2, 3, 4, 5]
list3[2] = 10
print(list3)
print("")


print("3. リスト `[1, 2, 3, 4, 5]` から要素 `3` を削除してください。")
list4 = [1, 2, 3, 4, 5]
list4.remove(3)
print(list4)
print("")

print("4. リスト `[1, 2, 3, 4, 5]` を逆順にしてください。")
list5 = [1, 2, 3, 4, 5]
list5.reverse()
print(list5)
print("")

### 18. リストの操作（応用）

print("1. リスト `[1, 2, 3, 4, 5]` の要素を全て2倍にするコードを書いてください。")
list6 = [1, 2, 3, 4, 5]
list6 = [number * 2 for number in list6]
print(list6)

print("")

print("2. リスト `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` から偶数だけを取り出して新しいリストを作成してください。")
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list8 = []
for number in list7:
    if number % 2 == 0:
        list8.append(number)
print(list8)
print("")

print("3. 文字列リスト `['apple', 'banana', 'cherry']` の各要素の長さを表示してください。")
list9 = ['apple', 'banana', 'cherry']
for item in list9:
    print(len(item))
print("")

print("4. リスト `[1, 2, 3, 4, 5]` と `[6, 7, 8, 9, 10]` を結合してください。")
list10 = [1, 2, 3, 4, 5]
list11 = [6, 7, 8, 9, 10]
list_sum = list10 + list11
print(list_sum)
print("")

### 19. リスト内包表記
print("1. リスト `[1, 2, 3, 4, 5]` の各要素を3倍にした新しいリストを作成してください。")
list12 = [1, 2, 3, 4, 5]
list13 = []

for number in list12:
    number_x3 = number * 3
    list13.append(number_x3)
print(list13)
print("")

print("2. リスト `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` から奇数だけを取り出して新しいリストを作成してください。")
list14 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list15 = []

for number in list14:
    if number %2 != 0:
        list15.append(number)
print(list15)
print("")
