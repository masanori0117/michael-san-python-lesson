### 81. ATMを作成しよう

print("コマンドラインから実行すること")
print("要件定義")
print("・残額、入金、引き出しの機能を実装")
print("実際にATMに必要な機能をリストアップして、ご自由に開発してみてください！")


class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"現在の残高: {self.balance}円")

    def check_amount(self, value):
        amount = input(value)
        if amount.isdigit():
            return int(amount)
        else:
            print("無効な金額です。数字を記入してください")
            return self.check_amount(value)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}円を入金しました。")
            print(f"預金残高: {self.balance}円")
        else:
            print("無効な金額です。")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount}円を引き出しました。")
            print(f"預金残高: {self.balance}円")
        elif amount > self.balance:
            print("残高不足です。")
        else:
            print("無効な金額です。")


def main(atm):

    print("\nATMメニュー:")
    print("1: 残高照会")
    print("2: 入金")
    print("3: 引き出し")
    print("4: 終了")

    choice = input("選択してください (1-5): ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = atm.check_amount("入金額を入力してください: ")
        atm.deposit(amount)
    elif choice == "3":
        amount = atm.check_amount("引き出し額を入力してください: ")
        atm.withdraw(amount)
    elif choice == "4":
        print("ご利用ありがとうございました。")
        return
    else:
        print("無効な選択です。")

    main(atm)

if __name__ == "__main__":
    atm = ATM(initial_balance=10000)
    main(atm)
