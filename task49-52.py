# 49. 辞書の内包表記
'''
以下のリストから辞書を作成してください。キーは要素そのもので、値はその要素の長さとします：
words = ["apple", "banana", "cherry"]
作成した辞書を出力してください。
'''

words = ["apple", "banana", "cherry"]

words_dict = {word: len(words) for word in words}
print(words_dict)

# 50. 複雑な辞書の操作
'''
以下の辞書が与えられています：

data = {
    "user1": {"name": "Ivy", "age": 29},
    "user2": {"name": "Jack", "age": 34},
    "user3": {"name": "Kate", "age": 25},
}
すべてのユーザーの名前をリストとして取得し、出力してください。
'''

data = {
    "user1": {"name": "Ivy", "age": 29},
    "user2": {"name": "Jack", "age": 34},
    "user3": {"name": "Kate", "age": 25},
}

user_names = []

for user_info in data.values():
    user_names.append(user_info["name"])
print(user_names)

# 51. デフォルト値の取得
'''
以下の辞書からキー "country" を取得してください。ただし、そのキーが存在しない場合は "Unknown" を返すようにしてください：

person = {"name": "Lily", "age": 30}
'''

person = {"name": "Lily", "age": 30}
country = person.get("country", "Unknown")
print(country)


# 52. ネストされた辞書の値取得
'''
以下の辞書から、ユーザー2の名前を取得してください：

data = {
    "user1": {"name": "Mike", "age": 27},
    "user2": {"name": "Nina", "age": 31},
    "user3": {"name": "Oscar", "age": 22},
}
'''

data = {
    "user1": {"name": "Mike", "age": 27},
    "user2": {"name": "Nina", "age": 31},
    "user3": {"name": "Oscar", "age": 22},
}

print(data["user2"]["name"])

