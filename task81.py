### 81. ATMを作成しよう

print("コマンドラインから実行すること")
print("要件定義")
print("・残額、入金、引き出しの機能を実装")
print("実際にATMに必要な機能をリストアップして、ご自由に開発してみてください！")


class ATM:

    CHECK_BALANCE = "1"
    DEPOSIT = "2"
    WITHDRAW = "3"
    EXIT = "4"

    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"現在の残高: {self.balance}円")

    def input_valid_amount(self, value):
        amount = input(value)
        if amount.isdigit():
            return int(amount)
        else:
            print("無効な金額です。正の数字を記入してください")
            return self.input_valid_amount(value)

    def is_valid_deposit(self, amount):
        return amount > 0

    def is_valid_withdraw(self, amount):
        if amount <= 0:
            print("無効な金額です。正の数を入力してください。")
            return False
        if amount > self.balance:
            print("残高不足です。引き出しできません。")
            return False
        return True

    def deposit(self):
        amount = self.input_valid_amount("入金額を入力してください: ")
        if self.is_valid_deposit(amount):
            self.balance += amount
            print(f"{amount}円を入金しました。")
            print(f"預金残高: {self.balance}円")
        else:
            print("無効な金額です。")

    def withdraw(self):
        amount = self.input_valid_amount("引き出し額を入力してください: ")
        if self.is_valid_withdraw(amount):
            self.balance -= amount
            print(f"{amount}円を引き出しました。")
            print(f"預金残高: {self.balance}円")

    def run(self):
        print("\nATMメニュー:")
        print(f"{self.CHECK_BALANCE}: 残高照会")
        print(f"{self.DEPOSIT}: 入金")
        print(f"{self.WITHDRAW}: 引き出し")
        print(f"{self.EXIT}: 終了")

        choice = input("選択してください (1-5): ")

        if choice == self.CHECK_BALANCE:
            self.check_balance()
            return self.run()
        elif choice == self.DEPOSIT:
            self.deposit()
            return self.run()
        elif choice == self.WITHDRAW:
            self.withdraw()
            return self.run()
        elif choice == self.EXIT:
            print("ご利用ありがとうございました。")
            return
        else:
            print("無効な選択です。")
            return self.run()

if __name__ == "__main__":
    atm = ATM(balance=10000)
    atm.run()
