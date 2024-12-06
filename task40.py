### 40. じゃんけん

### 下記の要件を満たす「じゃんけんプログラム」を開発してください。
### 要件定義
### ・使用可能な手はグー、チョキ、パー
### ・勝ち負けは、通常のじゃんけん
### ・Pythonファイルの実行はコマンドラインから。
### ご自身が自由に設計して、プログラムを書いてみましょう！

import random

def get_computer_hand():
    """
    ランダムにコンピューターの出し手を決定する

    Args:
        computer_hands (list): 選択肢の数字[1、 2、 3]の要素のリスト
    Returns:
        computer_hand (int): コンピューターの出し手に該当する数字を返す
    """
    computer_hands = [1, 2, 3]
    computer_hand = random.choice(computer_hands)
    return computer_hand

def input_user_hand():
    """
    ユーザーの出し手を入力させる

    Args:
        user_hands (str): ユーザーが入力したじゃんけんの出し手の入力値
    Returns:
        user_hand (int): ユーザーのじゃんけんの出し手に該当する数字 or 再帰関数でinput_user_handを再実行
    """
    user_hand = input("じゃんけん勝負！じゃんけんで出す手(1 = グー, 2 = チョキ, 3 = パー )を数字で選んでください。あなたの出し手: ")
    if check_user_hand(user_hand):
        return int(user_hand)
    return input_user_hand()

def check_user_hand(user_hand):
    """
    ユーザーのじゃんけんの出し手のバリデーションを実行
    """
    if user_hand.isdigit() and int(user_hand) in [1, 2, 3]:
        return True
    else:
        print("じゃんけんの出し手は1, 2, 3 のいずれかの数字を入力してください")
        return False

def display_hands(user_hand, computer_hand):
    """
    じゃんけんの出し手を出力する
    """
    user_hands = {1: "グー", 2: "チョキ", 3: "パー"}
    print(f"あなたの出し手: {user_hands[user_hand]}")
    print(f"コンピューターの出し手: {user_hands[computer_hand]}")


def display_winner(user_hand, computer_hand):
    """
    じゃんけんの勝者を出力する
    """
    if user_hand == computer_hand:
        print("あいこ")
    elif (user_hand == 1 and computer_hand == 2) or (user_hand == 2 and computer_hand == 3) or (user_hand == 3 and computer_hand == 1):
        print("あなたの勝ち!!")
    elif (user_hand == 1 and computer_hand == 3) or (user_hand == 2 and computer_hand == 1) or (user_hand == 3 and computer_hand == 2):
        print("あなたの負け")


def main():
    user_hand = input_user_hand()
    computer_hand = get_computer_hand()
    display_hands(user_hand, computer_hand)
    display_winner(user_hand, computer_hand)

if __name__ == "__main__":
    main()
