import random

print('ROCK, PAPER, SCISSORS')
print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

# initializing the variables
win = 0
lose = 0
tie = 0
moves = ['R', 'P', 'S']
winning_moves = [('R', 'S'), ('P', 'R'), ('S', 'P')]    #the required combination of user and generated move for user to win

while True:
    print(f'{win} Wins, {lose} Losses, {tie} Ties')     #to print status of win, lose, and tie
    RPS = random.choice(moves)                          #to generate random move from moves
    move = input('Enter your move: ').upper()
    if move in moves:
        print(move, 'vs', RPS)
        if move == RPS:
            tie += 1
            print("Tie")
        elif (move, RPS) in winning_moves:              #checking if inputed(current) combination is in winning_moves
            win += 1
            print('you win')
        else:                                           #if given combination not in winning_moves then user lose
            lose += 1
            print('you lose') 

    elif move == 'Q':
        print('Game end')
        print(f'You win {win}times out of {win+tie+lose} games')    #while quitting final result of how many wins user achieve by playing how many times are shown
        break
    
    else:
        print('Invalid move.Please select from R, P, S')
