### 9. for文と条件式の組み合わせ3
## 20 ~ 50までの数字の中で2で割ったら奇数となる数字のみを出力してください
print("9. for文と条件式の組み合わせ3")
print("20 ~ 50までの数字の中で2で割ったら奇数となる数字のみを出力してください")
for number in range(20, 51):
    if number % 2 != 0:
        print(number)

### 10. for文と条件式の組み合わせ4
## 20 ~ 50までの数字の中で2で割ったら奇数となる数字の個数を出力してください
print("10. for文と条件式の組み合わせ4")
print("20 ~ 50までの数字の中で2で割ったら奇数となる数字の個数を出力してください")
count = 0
for number in range(20, 51):
    if number % 2 != 0:
        count += 1
print(count)


### 11. for文を使用した計算
## 1000未満の「3と7の倍数」は何個あるか　個数を出力してください
print("11. for文を使用した計算")
print("1000未満の「3と7の倍数」は何個あるか　個数を出力してください")
count = 0
for number in range(1, 1000):
    if ( number % 3 == 0) or (number % 7 == 0):
        count+= 1
print(count)


### 12. for文を使用した計算2
## 1000未満の「3と7の倍数」の5番目に大きい数を出力してください
print("2. for文を使用した計算2")
print("1000未満の「3と7の倍数」の5番目に大きい数を出力してください")
data_list = []
for number in range(1, 1000):
    if (number % 3 == 0) or (number % 7 ==0):
        data_list.append(number)
print(data_list[-5])
