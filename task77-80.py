print("### 77. 演算子のオーバーロード")
print("`Time`というクラスを作成し、`hours`と`minutes`という属性を持たせてください。このクラスで`+`演算子をオーバーロードして、2つの`Time`オブジェクトを足し合わせた結果を新しい`Time`オブジェクトとして返すようにしてください。時間と分の加算が正しく行われるようにしてください（60分を超えた場合は1時間に繰り上げ）。")

class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        new_hours = self.hours + other.hours + extra_hours
        return Time(new_hours, new_minutes)

    def __str__(self):
        return f"{self.hours:02d}時間{self.minutes:02d}分"

time1 = Time(2, 45)
time2 = Time(1, 30)
time3 = time1 + time2
print(time3)


print("### 78. データクラス")
print("`dataclasses`モジュールを使用して、`Person`クラスをデータクラスとして作成してください。このクラスは`name`と`age`の属性を持ち、コンストラクタ、`__repr__`、`__eq__`メソッドを自動生成させてください。")

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person(name="田中", age=30)
p2 = Person(name="佐藤", age=40)
p3 = Person(name="鈴木", age=50)

print(p1)
print(p1 == p1)
print(p1 == p2)
print(p1 == p3)


print("### 79. シングルトンパターン")
print("`Singleton`というクラスを作成し、このクラスが常に1つのインスタンスしか生成されないようにしてください。複数のインスタンスを作成しようとした場合、最初に作成したインスタンスが返されるようにしてください。")

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'value'):
            self.value = value

s1 = Singleton(10)
s2 = Singleton(20)
print(s1.value)
print(s2.value)
print (s1 is s2)


print("### 80. ミックスインの使用")
print('`LoggableMixin`というクラスを作成し、`log`というメソッドを持たせてください。このメソッドは`"ログ出力: {message}"`と表示します。次に、`User`というクラスを作成し、この`LoggableMixin`をミックスインとして使用して`User`クラスにログ出力機能を追加してください。')

class LoggableMixin:

    def log(self, message):
        print(f"ログ出力: {message}")

class User(LoggableMixin):
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"User:{self.name}")

user = User("山田")
user.display_name()
user.log("名前を表示しました")






