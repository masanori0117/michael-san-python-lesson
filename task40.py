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

DRAW = 0
USER_WIN = 1
COMPUTER_WIN = 2

HAND_OPTIONS = (
    f"{STONE} = {HAND_TYPES[STONE]}, "
    f"{SCISSORS} = {HAND_TYPES[SCISSORS]}, "
    f"{PAPER} = {HAND_TYPES[PAPER]}"
)

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
    user_hand = input(f"じゃんけん勝負！じゃんけんで出す手({HAND_OPTIONS})を数字で選んでください。あなたの出し手: ")
    if not check_user_hand(user_hand):
        return input_user_hand()
    return int(user_hand)

def check_user_hand(user_hand):
    """
    ユーザーのじゃんけんの出し手のバリデーションを実行
        returns:
            bool: 有効な出し手なら True、無効な場合は False
    """

    if not user_hand.isdigit():
        print("じゃんけんの出し手は数字を入力してください")
        return False
    if int(user_hand) not in HAND_TYPES:
        print("じゃんけんの出し手は0, 1, 2 のいずれかの数字を入力してください")
        return False
    return True

def display_hands(user_hand, computer_hand):
    """
    じゃんけんの出し手を出力する
    """
    print(f"あなたの出し手: {HAND_TYPES[user_hand]}")
    print(f"コンピューターの出し手: {HAND_TYPES[computer_hand]}")


def judge(user_hand, computer_hand):
    """
    勝敗を判定する

    Args:
        user_hand (int): ユーザーの出し手を表す数字 (0: グー, 1: チョキ, 2: パー）
        computer_hand (int): コンピューターの出し手を表す数字 (0: グー, 1: チョキ, 2: パー）

    Returns:
        int: 0:引き分け , 1: ユーザーのかち, 2:コンピューターの勝ち
    """

    return (user_hand - computer_hand + 3) % 3


def display_winner(result):
    """
    じゃんけんの勝者を出力する
    """
    if result == DRAW:
        print("あいこ")
    elif result == USER_WIN:
        print("あなたの勝ち!!")
    elif result == COMPUTER_WIN:
        print("あなたの負け")

def should_retry():
    """
    ゲームをもう一度プレイするか確認する

    Returns:
        bool: ゲームを再度プレイする場合は True、終了する場合は False
    """
    retry = input("もう一度プレイしますか？ (y/n): ")
    return retry.lower() == 'y'

def play_game():
    """
    1回分のじゃんけんゲームをプレイする
    """
    user_hand = input_user_hand()
    computer_hand = get_computer_hand()
    display_hands(user_hand, computer_hand)
    result = judge(user_hand, computer_hand)
    display_winner(result)

def main():
    """
    ゲームのメイン処理
    """
    play_game()
    while should_retry():
        play_game()
    print("ゲームを終了します。")

if __name__ == "__main__":
    main()
