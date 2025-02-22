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
    SELECT_PROMPT = "選択してください (1-4): "
    THANK_YOU_MESSAGE = "ご利用ありがとうございました。"
    DEPOSIT_AMOUNT_PROMPT = "入金額を入力してください: "
    WITHDRAW_AMOUNT_PROMPT = "引き出し額を入力してください: "


class InputValidation:
    def validate(self, amount):
        if not isinstance(amount, str):
            amount = str(amount)
        return amount.isdigit() and int(amount) > 0


class DepositValidation(InputValidation):
    def validate(self, amount):
        return super().validate(amount)


class WithdrawValidation(InputValidation):
    def validate(self, amount, balance):
        return super().validate(amount) and int(amount) <= balance


class ATM:
    SHOW_BALANCE = "1"
    DEPOSIT = "2"
    WITHDRAW = "3"
    EXIT = "4"

    def __init__(self, balance=0):
        self.balance = balance
        self.deposit_validation = DepositValidation()
        self.withdraw_validation = WithdrawValidation()

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

    def input_amount(self, prompt):
        amount = input(prompt)
        if self.deposit_validation.validate(amount):
            return int(amount)
        print(ErrorMessage.INVALID_INPUT_AMOUNT)
        return self.input_amount(prompt)

    def deposit(self):
        amount = self.input_amount(OperationPrompt.DEPOSIT_AMOUNT_PROMPT)
        if self.deposit_validation.validate(amount):
            self.balance += amount
            print(f"{amount}円を入金しました。")
            print(f"預金残高: {self.balance}円")

    def withdraw(self):
        amount = self.input_amount(OperationPrompt.WITHDRAW_AMOUNT_PROMPT)
        if self.withdraw_validation.validate(amount, self.balance):
            self.balance -= amount
            print(f"{amount}円を引き出しました。")
            print(f"預金残高: {self.balance}円")
        else:
            print(ErrorMessage.INSUFFICIENT_AMOUNT)


if __name__ == "__main__":
    atm = ATM(balance=10000)
    atm.run()
