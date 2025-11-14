from collections import Counter

def predict_player_move(player_history):
    if not player_history:
        return None

    counts = Counter(player_history)
    predicted = counts.most_common(1)[0][0]
    return predicted

def counter_move(predicted_player_move):
    if predicted_player_move is None:
        return "R"

    if predicted_player_move == "R":
        return "P"
    elif predicted_player_move == "P":
        return "S"
    else:
        return "R" 

def statistics_ai_move(player_history):
    predicted = predict_player_move(player_history)
    return counter_move(predicted)
