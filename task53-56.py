### 53. シャローコピーとディープコピー
'''
以下の辞書をシャローコピーし、ディープコピーしてください。

またシャローコピーした後、ディープコピーした後のoriginalをそれぞれ出力し、動作の違いを確認してください。

```python

original = {"a": {"nested": 1}, "b": 2}

```
---
'''

import copy

original = {"a": {"nested": 1}, "b": 2}

shallow_copy = copy.copy(original)
deep_copy_after_shallow = copy.deepcopy(shallow_copy)

deep_copy = copy.deepcopy(original)
shallow_copy_after_deep = copy.copy(deep_copy)

print("Original:", original)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
print("Deep copy after shallow copy:", deep_copy_after_shallow)
print("Shallow copy after deep copy:", shallow_copy_after_deep)


### 54. 辞書のキーでソート
'''
以下の辞書をキーでソートしてください：

```python
scores = {"Charlie": 85, "Alice": 92, "Bob": 78}
```
---
'''

scores = {"Charlie": 85, "Alice": 92, "Bob": 78}
sorted_scores = dict(sorted(scores.items()))
print(sorted_scores)


### 55. 辞書の値でソート
'''
以下の辞書を値でソートしてください：

```python
scores = {"Charlie": 85, "Alice": 92, "Bob": 78}
```
---
'''

scores = {"Charlie": 85, "Alice": 92, "Bob": 78}
sorted_scores = dict(sorted(scores.items(),key=lambda item: item[1]))
print(sorted_scores)


### 56. 辞書の比較
'''
以下の辞書2つが等しいか確認してください：

```python

dict1 = {"x": 10, "y": 20}
dict2 = {"y": 20, "x": 10}

```
'''

dict1 = {"x": 10, "y": 20}
dict2 = {"y": 20, "x": 10}
are_equal = dict1 == dict2
print(are_equal)




