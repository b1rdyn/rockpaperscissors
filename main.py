from ai_multi import MultiAI, score_for_ai

MOVE_NAMES = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors",
}

def main():
    print("Welcome to Rock Paper Scissors!")
    print("Choose [R]ock [P]aper or [S]cissors. [Q]uit.")

    ai = MultiAI(focus_length=5)
    player_score = 0
    ai_score = 0

    while True:
        choice = input("> ").strip().upper()

        if choice == "Q":
            print(f"Final score: You {player_score} - AI {ai_score}")
            break

        if choice not in ("R", "P", "S"):
            print("Invalid input.")
            continue

        player_move = choice
        ai_move = ai.choose_move()

        print(f"AI played: {MOVE_NAMES[ai_move]} ({ai_move})")

        result = score_for_ai(ai_move, player_move)
        if result == 1:
            ai_score += 1
            outcome = "You lose!"
        elif result == -1:
            player_score += 1
            outcome = "You win!"
        else:
            outcome = "Draw!"

        print(f"{outcome} Score: You {player_score} - AI {ai_score}\n")
        ai.update(player_move)


if __name__ == "__main__":
    main()
