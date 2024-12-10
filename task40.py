### 40. じゃんけん

### 下記の要件を満たす「じゃんけんプログラム」を開発してください。
### 要件定義
### ・使用可能な手はグー、チョキ、パー
### ・勝ち負けは、通常のじゃんけん
### ・Pythonファイルの実行はコマンドラインから。
### ご自身が自由に設計して、プログラムを書いてみましょう！

import random

STONE = 0
SCISSORS = 1
PAPER = 2

HAND_TYPES = {
STONE: "グー",
SCISSORS: "チョキ",
PAPER: "パー",
}

def get_computer_hand():
    """
    ランダムにコンピューターの出し手を決定する

    Returns:
        computer_hand (int): コンピューターの出し手に該当する数字を返す
    """

    return random.choice(list(HAND_TYPES.keys()))

def input_user_hand():
    """
    ユーザーの出し手を入力させる

    Args:
        user_hands (str): ユーザーが入力したじゃんけんの出し手の入力値
    Returns:
        user_hand (int): ユーザーのじゃんけんの出し手に該当する数字 or 再帰関数でinput_user_handを再実行
    """
    user_hand = input("じゃんけん勝負！じゃんけんで出す手(0 = グー, 1 = チョキ, 2 = パー )を数字で選んでください。あなたの出し手: ")
    if check_user_hand(user_hand):
        return int(user_hand)
    return input_user_hand()

def check_user_hand(user_hand):
    """
    ユーザーのじゃんけんの出し手のバリデーションを実行
        returns:
            bool: 有効な出し手なら True、無効な場合は False
    """

    try:
        user_hand = int(user_hand)
        if int(user_hand) in HAND_TYPES:
            return True
    except ValueError:
        pass
    print("じゃんけんの出し手は0, 1, 2 のいずれかの数字を入力してください")
    return False

def display_hands(user_hand, computer_hand):
    """
    じゃんけんの出し手を出力する
    """
    print(f"あなたの出し手: {HAND_TYPES[user_hand]}")
    print(f"コンピューターの出し手: {HAND_TYPES[computer_hand]}")


def judge(user_hand, computer_hand):
    """
    勝敗を判定する

    Returns:
        int: 0:引き分け , 1: ユーザーのかち, 2:コンピューターの勝ち
    """

    return (user_hand - computer_hand + 3) % 3


def display_winner(result):
    """
    じゃんけんの勝者を出力する
    """
    if result == 0:
        print("あいこ")
    elif result == 1:
        print("あなたの勝ち!!")
    elif result == 2:
        print("あなたの負け")


def main():
    user_hand = input_user_hand()
    computer_hand = get_computer_hand()
    display_hands(user_hand, computer_hand)
    result = judge(user_hand, computer_hand)
    display_winner(result)

if __name__ == "__main__":
    main()
