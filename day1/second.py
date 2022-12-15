with open("input2.txt","r") as f:
    x = f.read().splitlines()

print(x)
'''
scores

The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
(0 if you lost, 3 if the round was a draw, and 6 if you won).

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).

In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
This ends in a loss for you with a score of 1 (1 + 0).

The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

'''
scoretable = {"A":1,"B":2,"C":3, "X":1,"Y":2,"Z":3}
win_draw_lost = {
    "A X":3,
    "A Y":6,
    "A Z":0,
    "B X":0,
    "B Y":3,
    "B Z":6,
    "C X":6,
    "C Y":0,
    "C Z":3,
}

my_s_sum = 0
for score in x:
    opponent_move,my_move = score.split(" ")
    my_score = win_draw_lost[score]+scoretable[my_move]
    my_s_sum+=my_score
print(my_s_sum)

    #check who wins
'''
    R,P,S = AX,BY,CZ
    A X = draw, 3
    A Y = win, 6
    A Z = lose, 0
    B X = lose, 0
    B Y = draw, 3
    B Z = win, 6
    C X = win, 6
    C Y = lose, 0
    C Z = draw, 3
    '''
