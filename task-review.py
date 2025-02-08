print("### 78. データクラス")
print("`dataclasses`モジュールを使用して、`Person`クラスをデータクラスとして作成してください。このクラスは`name`と`age`の属性を持ち、コンストラクタ、`__repr__`、`__eq__`メソッドを自動生成させてください。")

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person(name="田中", age = 30)
p2 = Person(name="鈴木", age = 40)
p3 = Person(name="佐藤", age = 50)

print(p1)
print(p2)
print(p3)


print("### 79. シングルトンパターン")
print("`Singleton`というクラスを作成し、このクラスが常に1つのインスタンスしか生成されないようにしてください。複数のインスタンスを作成しようとした場合、最初に作成したインスタンスが返されるようにしてください。")

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'value'):
            self.value = value

s1 = Singleton(10)
s2 = Singleton(20)

print(s1.value)
print(s2.value)
print(s1 is s2)


print("### 80. ミックスインの使用")
print('`LoggableMixin`というクラスを作成し、`log`というメソッドを持たせてください。このメソッドは`"ログ出力: {message}"`と表示します。次に、`User`というクラスを作成し、この`LoggableMixin`をミックスインとして使用して`User`クラスにログ出力機能を追加してください。')

class LoggableMixin:

    def log(self, message):
        print(f"ログ出力: {message}")

class User(LoggableMixin):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"名前: {self.name}"

user1 = User("山田")
print(user1)
user1.log("Userインスタンスを作成しました")













































