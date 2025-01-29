### 65. クラス内で別のクラスを使用する
print("`Engine`というクラスを作成し、以下の属性を持たせてください:")
print("- `horsepower`: 整数")
print("次に`Car`クラスを作成し、`Engine`クラスのインスタンスを`engine`属性として持たせてください。`Car`クラスの`get_engine_power`というメソッドで`horsepower`を返すようにしてください。")

class Engine:

    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:

    def __init__(self, horsepower):
        self.engine = Engine(horsepower)

    def get_engine_power(self):
        return self.engine.horsepower

car = Car(25)
print(car.get_engine_power())


### 66. クラス変数の使用
print("`Student`クラスを作成し、`name`（文字列）と`score`（整数）の属性を持たせてください。また、全体の生徒数をカウントするためのクラス変数`student_count`を追加してください。インスタンスが作成されるたびに`student_count`が1増えるようにしてください。")

class Student:

    student_count = 0
    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.student_count += 1

student1 = Student("田中", 25)
student2 = Student("佐藤", 20)
student3 = Student("鈴木", 30)
print(Student.student_count)


### 67. プロパティの使用
print("`BankAccount`クラスを作成し、`balance`（残高）をプライベートな属性として持たせてください。また、`deposit`（預入）と`withdraw`（引出）のメソッドを作成し、プロパティ`balance`を介して残高を取得できるようにしてください。")

class BankAccount:

    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    @property
    def balance(self):
        """
        残高をプロパティとして取得
        """
        return self.__balance

    def deposit(self, amount):
        """
        預入メソッド
        amountが負の値の場合はエラー表示
        """
        if amount < 0:
            print("預け入れ金額は正の数である必要があります。")
            return
        self.__balance += amount

    def withdraw(self, amount):
        """
        引出メソッド
        amountが負の値の場合はエラー表示
        現在の残高を超える場合もエラー表示
        """
        if amount < 0:
            print("預け入れ金額は正の数である必要があります。")
            return
        if amount > self.__balance:
            print("残高が不足しています。")
            return
        self.__balance -= amount

if __name__ == "__main__":

    account = BankAccount(10000)
    print(f"初期残高: {account.balance}")
    account.deposit(5000)
    account.withdraw(1000)
    print(f"取引後後残高: {account.balance}")

### 68. 演算子のオーバーロード
print("`Vector`というクラスを作成し、2つの属性`x`と`y`を持たせてください。このクラスで`+`演算子をオーバーロードして、2つの`Vector`オブジェクトを足し合わせて新しい`Vector`を返すようにしてください。")

class Vector:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        number も Vector クラスのインスタンスを想定。
        self.x + other.x, self.y + other.y の結果を持つ新しい Vector を返す
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        """
        オブジェクトを print() などで表示したときにわかりやすい文字列を返す
        """
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
print(f"v1: {v1}")
v2 = Vector(3, 4)
print(f"v2: {v2}")
v3 = v1 + v2
print(f"v3: {v3}")





