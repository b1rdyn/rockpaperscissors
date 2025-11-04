from collections import Counter

def predict_next_move(player_history):
    if not player_history:
        return "Rock"

    counts = Counter(player_history)
    predicted = counts.most_common(1)[0][0]

    if predicted == "Rock":
        return "Paper"
    elif predicted == "Paper":
        return "Scissors"
    else:
        return "Rock"
