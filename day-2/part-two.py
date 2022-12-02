# first column = opponent
#  A for Rock, B for Paper, and C for Scissors.

# second column = my play
# X = you have to lose, Y = draw, Z = win 

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# same shape = draw

# one_round_score =
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# + outcome (0 = lose, 3 = draw, 6 = won)

# return TOTAL SCORE (sum of all one_round_score for me)

def main():
    shapes = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
    must_outcomes = {'X': 'lose', 'Y': 'draw', 'Z': 'win'} 
    must_scores = {'lose': 0, 'draw': 3, 'win': 6}
    shape_values = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

    # plays go like.. "opponent plays... I play... result score"
    plays = {'Rock': {'Rock': 3, 'Paper': 6, 'Scissors': 0},
             'Paper': {'Paper': 3, 'Rock': 0, 'Scissors': 6},
             'Scissors': {'Scissors': 3, 'Rock': 6, 'Paper': 0}}

    # reverse plays are ... if opponent plays Shape, and I must <play>, then I play <Shape>
    reverse_plays = {'Rock': {'lose': 'Scissors', 'draw': 'Rock', 'win': 'Paper'},
                     'Paper': {'lose': 'Rock', 'draw': 'Paper', 'win': 'Scissors'},
                     'Scissors': {'lose': 'Paper', 'draw': 'Scissors', 'win': 'Rock'}}


    # read in input.txt into list
    with open('input.txt', 'r') as f:
        # read input into list of lines
        lines = f.readlines()
        # strip whitespace from each line
        lines = [line.strip() for line in lines]
        sanitized = [line.split(' ') for line in lines]
    total_score = 0 
    i = 1 
    for round in sanitized:
        opponent_raw = round[0]
        opponent = shapes[opponent_raw]
        my_outcome = round[1]
        must_outcome = must_outcomes[my_outcome]
        print('Round {}: opponent played {}, I must {}.'.format(i, opponent, must_outcome))
        my_played_shape = reverse_plays[opponent][must_outcome]
        total_score = total_score + shape_values[my_played_shape] + must_scores[must_outcome]
        i = i +1 
    print(total_score)

if __name__ == '__main__':
    main()
