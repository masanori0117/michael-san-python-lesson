### 57. 辞書内包表記による削除
print("以下の辞書から値が100未満のキーと値を削除してください：")

prices = {"apple": 150, "banana": 90, "cherry": 200}
prices = {key: value for key,value in prices.items() if value >= 100}
print(prices)


### 58. キーと値の入れ替え
print("以下の辞書でキーと値を入れ替えた新しい辞書を作成してください：")

original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(inverted)


### 59. リストを辞書に変換
print("以下のリストを辞書に変換してください。リストの偶数インデックスの要素をキー、奇数インデックスの要素を値とします：")

data = ["name", "Alice", "age", 25, "city", "Tokyo"]
data_dictionalized = {data[num]: data[num + 1] for num in range(0, len(data), 2)}
print(data_dictionalized)


### 60. 辞書を使ったグルーピング
print("以下のリストを値ごとにグルーピングした辞書を作成してください：")

data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot"), ("fruit", "cherry")]
grouped_data = {}
for category, value in data:
    if category not in grouped_data:
        grouped_data[category] = []
    grouped_data[category].append(value)
print(grouped_data)