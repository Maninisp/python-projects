import random

print('ROCK, PAPER, SCISSORS')
print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

moves = ['R', 'P', 'S']
winning_moves = [('R', 'S'), ('P', 'R'), ('S', 'P')]
win = 0
lose = 0
tie = 0

while True:
    print(f'{win} Wins, {lose} Losses, {tie} Ties')
    RPS = random.choice(moves)
    move = input('Enter your move: ').upper()
    if move in moves:
        print(move, 'vs', RPS)
        if move == RPS:
            tie += 1
            print("Tie")
        elif (move, RPS) in winning_moves:
            win += 1
            print('you win')
        else:
            lose += 1
            print('you lose') 
    elif move == 'Q':
        print('Game end')
        print(f'You win {win}times out of {win+tie+lose} games')
        break
    else:
        print('Invalid move.Please select from R, P, S')