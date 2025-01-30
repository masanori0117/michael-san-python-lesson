print("### 69. クラスメソッドの使用")
print("`Employee`クラスを作成し、`name`と`salary`の属性を持たせてください。また、クラスメソッド`create_employee`を作成し、`name`と`salary`を引数として新しい`Employee`オブジェクトを生成する静的な方法を提供してください。")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def create_employee(cls, name, salary):
        return cls(name, salary)

employ1 = Employee.create_employee("Alice", 50000)
print(employ1.name, employ1.salary)


print("")
print("")
print("### 70. スタティックメソッドの使用")
print("`MathOperations`というクラスを作成し、`add`と`multiply`という2つのスタティックメソッドを作成してください。これらのメソッドは2つの数値を受け取り、それぞれ足し算と掛け算を行うものとします。")

class MathOperations:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    def multiply(num1, num2):
        return num1 * num2

print(MathOperations.add(5, 2))
print(MathOperations.multiply(3, 5))

print("")
print("")
print("### 71. 特殊メソッド（`__str__`と`__repr__`）")
print("`Book`というクラスを作成し、以下の属性を持たせてください:")
print("- `title`: 文字列")
print("- `author`: 文字列")
print("このクラスで`__str__`と`__repr__`の特殊メソッドを実装し、`print()`関数でオブジェクトを出力したときに、`__str__`では `タイトル: {title}, 著者: {author}` の形式で表示され、`__repr__`では `Book('{title}', '{author}')` の形式で表示されるようにしてください。")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"タイトル: {self.title}, 著者: {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("我輩は猫である", " 夏目漱石")
print(str(book))
print(repr(book))


print("")
print("")
print("### 72. 継承とポリモーフィズム")
print("`Shape`という抽象クラスを作成し、`area`という抽象メソッドを定義してください。次に、`Circle`（円）と`Rectangle`（長方形）という2つのクラスを`Shape`クラスから継承し、それぞれの`area`メソッドを実装してください。")
print("- `Circle`クラスには`radius`（半径）を持たせ、面積を計算してください。")
print("- `Rectangle`クラスには`width`（幅）と`height`（高さ）を持たせ、面積を計算してください。")

from abc import ABC, abstractmethod

@abstractmethod
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
print(circle.area())

rectangle = Rectangle(3, 5)
print(rectangle.area())


