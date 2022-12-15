with open("input.txt","r") as f:
    x = f.read().splitlines()

# print(x[0])

'''
X lose
Y draw
Z win

A X means opponent does A(Rock) and i have to X(lose) so i must do B(Paper)

'''
scoretable = {"A":1,"B":2,"C":3}

ldw = ["A","B","C"] #loss draw win gives me what to choose for what opponent chooses to LOSE or DRAW or WIN
                    #contains possible moves A,B,C = R,P,S
my_total_scores = 0
for scre in x:
    my_score = 0
    opponent_move, end_res = scre.split(" ")
    if end_res == "X":      #lose
        my_move = ldw[(ldw.index(opponent_move)-1)%3]

    elif end_res == "Z":    #win
        my_move = ldw[(ldw.index(opponent_move)+1)%3]
        my_score+=6

    else:                   #draw
        my_move = opponent_move
        my_score+=3

    # so i need to add my score as stated by the win draw or lose + points by my move as in scoretable
    my_total_scores+=my_score+scoretable[my_move]

print(my_total_scores)
