print("### 73. プロパティを使用したクラス")
print("`Temperature`というクラスを作成し、`celsius`という属性を持たせてください。`fahrenheit`というプロパティを作成し、摂氏（Celsius）から華氏（Fahrenheit）への変換を行うゲッターを実装してください。また、`fahrenheit`のセッターを作成し、華氏から摂氏に変換して`celsius`に値を設定できるようにしてください。")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"摂氏:{temp.celsius}℃")
print(f"華氏:{temp.fahrenheit}℉")

temp.fahrenheit = 96.8
print(f"変更後の華氏:{temp.celsius}℃")


print("### 74. クラスメソッドとスタティックメソッドの違い")
print("`Calculator`というクラスを作成し、以下のメソッドを持たせてください:")
print("- `@staticmethod`として`add(a, b)`と`multiply(a, b)`を作成し、それぞれ足し算と掛け算を行う。")
print("- `@classmethod`として`info()`を作成し、`'これはCalculatorクラスです'`というメッセージを出力する。")

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @classmethod
    def info(cls):
        print('これはCalculatorクラスです')

print(Calculator.add(2, 3))
print(Calculator.multiply(2, 3))
Calculator.info()

print("### 75. 抽象クラス")
print('`Vehicle`という抽象クラスを作成し、`move`という抽象メソッドを定義してください。次に、このクラスを継承して`Car`と`Bicycle`というクラスを作成し、それぞれの`move`メソッドを実装してください。`Car`では`"車が走ります"`、`Bicycle`では`"自転車が走ります"`と表示されるようにしてください。')

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("車が走ります")


class Bicycle(Vehicle):
    def move(self):
        print("自転車が走ります")

car = Car()
bicycle = Bicycle()

car.move()
bicycle.move()

### 76. デコレータの利用
print("`Product`というクラスを作成し、`price`という属性を持たせてください。次に、`price_with_tax`というプロパティを作成し、消費税を加えた金額を返すゲッターを実装してください。消費税率は8%として計算してください。")

class Product:
    tax_rate = 0.08

    def __init__(self, price):
        self.price = price

    @property
    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

price = Product(100)
print(price.price_with_tax)






