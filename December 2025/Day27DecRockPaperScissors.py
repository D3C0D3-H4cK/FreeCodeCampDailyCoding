def rock_paper_scissors(player1, player2):

    if player1 == player2:
        print("Tie")
    if player1 == "Rock" and player2 == "Scissors":
        return "Player 1 wins"
    elif player1 == "Paper" and player2 == "Rock":
        return "Player 1 wins"
    elif player1 == "Scissors" and player2 == "Paper":
        return "Player 1 wins"
    else:
        return "Player 2 wins"
rock_paper_scissors("Rock", "Rock")