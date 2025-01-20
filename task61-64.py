### 61. 基本的なクラスの作成
print("Personというクラスを作成してください。このクラスには以下の属性があります:")
print("name: 文字列")
print('age: 整数 introduceというメソッドを作成し、"私の名前は{name}で、{age}歳です。"というメッセージを出力するようにしてください。')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"私の名前は{self.name}で、{self.age}歳です。")

tanaka = Person("田中", 25)
tanaka.introduce()


### 62. コンストラクタを持つクラスの作成
print("Carというクラスを作成し、以下の属性を持たせてください:")
print("brand: 文字列")
print("model: 文字列")
print('year: 整数 コンストラクタでこれらの属性に初期値を設定できるようにし、get_infoというメソッドで"{brand} {model} ({year})"という形式で出力してください。')

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

car = Car("トヨタ", "プリウス", 2024)
car.get_info()


### 63. メソッドを持つクラス
print("Rectangleというクラスを作成し、以下の属性を持たせてください:")
print("width: 整数")
print("height: 整数 areaというメソッドを作成し、長方形の面積を計算して返すようにしてください。")

class Rectangle:
    def __init__(self, width, height):
        """
        長方形を表すクラス
        Args:
            width(int): 長方形の幅 (整数)
            height(int): 長方形の高さ (整数)
        """
        self.width = width
        self.height = height

    def area(self):
        """
        長方形の面積を計算して返す
        return:
            面積(int)
        """
        return self.width * self.height

rectangle = Rectangle(10, 20)
area_calculatiion = rectangle.area()
print(f"長方形の面積: {area_calculatiion}")


### 64. 継承を使用したクラス
print('Animalというクラスを作成し、speakというメソッドを作成して"動物の鳴き声"と表示するようにしてください。次に、DogというクラスをAnimalクラスを継承して作成し、speakメソッドをオーバーライドして"ワンワン"と表示するようにしてください。')

class Animal:
    def speak(self):
        """
        動物の鳴き声を返す
        return:
            動物の鳴き声(string)
        """
        return "動物の鳴き声"

class Dog(Animal):
    def speak(self):
        """
        犬の鳴き声を返す
        return:
            犬の鳴き声(string)
        """
        return "ワンワン"

animal = Animal()
print(animal.speak())

dog = Dog()
print(dog.speak())