print("### 41. 辞書の作成")
print('以下のキーと値を持つ辞書 `person` を作成してください：')
print(' - キー: "name", 値: "Alice" ')
print(' - キー: "age", 値: 25 ')
print(' - キー: "city", 値: "Tokyo" ')
print('作成した辞書を出力してください。')

dictionary = {"name": "Alice", "age": 25, "city": "Tokyo"}
print(dictionary)

print("### 42. 辞書から値を取得")

print('以下の辞書が与えられています：')
print('person = {"name": "Bob", "age": 30, "city": "Osaka"}')
print('キー `"age"` に対応する値を取得し、出力してください。')

person = {"name": "Bob", "age": 30, "city": "Osaka"}
print(person["age"])

print("### 43. 辞書に要素を追加")

print('以下の辞書に新しいキーと値 `"country": "Japan"` を追加してください：')
print('person = {"name": "Charlie", "age": 35, "city": "Kyoto"}')
print('変更後の辞書を出力してください。')

person = {"name": "Charlie", "age": 35, "city": "Kyoto"}
person["country"] = "Japan"
print(person)

print("### 44. 辞書の要素を削除")
print('以下の辞書からキー `"city"` を削除してください：')
print('person = {"name": "Diana", "age": 28, "city": "Nagoya"}')
print('変更後の辞書を出力してください。')

person = {"name": "Diana", "age": 28, "city": "Nagoya"}
del person["city"]
print(person)