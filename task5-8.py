### 5. for文の基礎
# 1~10までの数字をfor文を使って出力してください

for number in range(1, 11):
    print(number)

### 6. for文の基礎２
# 35 ~ 46までの数字をfor文を使って出力してください
for number in range(35, 47):
    print(number)


### 7.for文と条件式の組み合わせ
# 40 ~ 50までの数字の中で奇数の数字のみを出力してください
for number in range(40, 51):
    if number %2 != 0:
        print(number)

### 8. for文と条件式の組み合わせ2
# 10 ~ 25までの数字の中で3の倍数の数字のみを出力してください
for number in range(10, 26):
    if number %3 == 0:
        print(number)
