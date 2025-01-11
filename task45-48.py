### 45. キーの存在確認
print('以下の辞書が与えられています：')
print('person = {"name": "Eve", "age": 22}')
print('キー `"city"` が辞書に存在するか確認し、その結果を出力してください。')

person = {"name": "Eve", "age": 22}
if "city" in person:
    print(person["city"])
else:
    print('"city" というキーは存在しません')


### 46. 辞書のすべてのキーと値をループで取得
print('以下の辞書が与えられています：')
print('person = {"name": "Frank", "age": 40, "city": "Sapporo"}')
print('すべてのキーと値を `"キー: 値"` という形式で1行ずつ出力してください。')

person = {"name": "Frank", "age": 40, "city": "Sapporo"}
for key, value in person.items():
    print(f"{key} : {value}")


### 47. 辞書のマージ
print('以下の2つの辞書を1つにマージしてください：')
print('dict1 = {"name": "Grace", "age": 33}')
print('dict2 = {"city": "Kobe", "country": "Japan"}')
print('マージ後の辞書を出力してください。')

dict1 = {"name": "Grace", "age": 33}
dict2 = {"city": "Kobe", "country": "Japan"}
merged_dict = dict1 | dict2
print(merged_dict)


### 48. 辞書の値を更新
print('以下の辞書でキー `"age"` の値を `45` に更新してください：')
print('person = {"name": "Henry", "age": 40, "city": "Sendai"}')
print('更新後の辞書を出力してください。')

person = {"name": "Henry", "age": 40, "city": "Sendai"}
person["age"] = 45
print(person)