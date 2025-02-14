### 81. ATMを作成しよう

print("コマンドラインから実行すること")
print("要件定義")
print("・残額、入金、引き出しの機能を実装")
print("実際にATMに必要な機能をリストアップして、ご自由に開発してみてください！")


class ErrorMessage:
    INVALID_INPUT_AMOUNT = "無効な金額です。正の数字を記入してください"
    INVALID_COMMAND = "無効な選択です。"
    INSUFFICIENT_AMOUNT = "残高不足です。引き出しできません。"

class OperationPrompt:
    SELECT_PROMPT = "選択してください (1-5): "
    THANK_YOU_MESSAGE = "ご利用ありがとうございました。"
    DEPOSIT_AMOUNT_PROMPT = "入金額を入力してください: "
    WITHDRAW_AMOUNT_PROMPT = "引き出し額を入力してください: "

class Validation(OperationPrompt):
    @staticmethod
    def is_positive_number(value):
        return value.isdigit() and int(value) > 0

    @staticmethod
    def can_withdraw(amount, balance):
        return amount <= balance

    @staticmethod
    def is_valid_deposit(amount):
        if amount < 0:
            print(ErrorMessage.INVALID_INPUT_AMOUNT)
            return False
        return True

    @staticmethod
    def is_valid_withdraw(amount, balance):
        if amount <= 0:
            print(ErrorMessage.INVALID_INPUT_AMOUNT)
            return False
        if amount > balance:
            print(ErrorMessage.INSUFFICIENT_AMOUNT)
            return False
        return True

class ATM(ErrorMessage, OperationPrompt):

    SHOW_BALANCE = "1"
    DEPOSIT = "2"
    WITHDRAW = "3"
    EXIT = "4"

    def __init__(self, balance=0):
        self.balance = balance

    def run(self):
        print("\nATMメニュー:")
        print(f"{self.SHOW_BALANCE}: 残高照会")
        print(f"{self.DEPOSIT}: 入金")
        print(f"{self.WITHDRAW}: 引き出し")
        print(f"{self.EXIT}: 終了")

        choice = input(OperationPrompt.SELECT_PROMPT)

        if choice == self.SHOW_BALANCE:
            self.show_balance()
        elif choice == self.DEPOSIT:
            self.deposit()
        elif choice == self.WITHDRAW:
            self.withdraw()
        elif choice == self.EXIT:
            print(OperationPrompt.THANK_YOU_MESSAGE)
            return
        else:
            print(ErrorMessage.INVALID_COMMAND)
        return self.run()

    def show_balance(self):
        print(f"現在の残高: {self.balance}円")

    def input_amount(self, value):
        amount = input(value)
        if Validation.is_positive_number(amount):
            return int(amount)
        else:
            print(ErrorMessage.INVALID_INPUT_AMOUNT)
            return self.input_amount(value)

    def deposit(self):
        amount = self.input_amount(OperationPrompt.DEPOSIT_AMOUNT_PROMPT)
        if Validation.is_valid_deposit(amount):
            self.balance += amount
            print(f"{amount}円を入金しました。")
            print(f"預金残高: {self.balance}円")

    def withdraw(self):
        amount = self.input_amount(OperationPrompt.WITHDRAW_AMOUNT_PROMPT)
        if Validation.is_valid_withdraw(amount, self.balance):
            self.balance -= amount
            print(f"{amount}円を引き出しました。")
            print(f"預金残高: {self.balance}円")

if __name__ == "__main__":
    atm = ATM(balance=10000)
    atm.run()
