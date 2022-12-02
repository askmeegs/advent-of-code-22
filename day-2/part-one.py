# first column = opponent
#  A for Rock, B for Paper, and C for Scissors.

# second column = my play
# X for Rock, Y for Paper, and Z for Scissors

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# same shape = draw

# one_round_score =
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# + outcome (0 = lose, 3 = draw, 6 = won)

# return TOTAL SCORE (sum of all one_round_score for me)

def main():
    shapes = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
              'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
    # plays go like.. "opponent plays... I play... result score"
    plays = {'Rock': {'Rock': 3, 'Paper': 6, 'Scissors': 0},
             'Paper': {'Paper': 3, 'Rock': 0, 'Scissors': 6},
             'Scissors': {'Scissors': 3, 'Rock': 6, 'Paper': 0}}

    shape_values = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

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
        opponent = round[0]
        my_play = round[1]
        o_shape = shapes[opponent]
        my_shape = shapes[my_play]
        print("Round {}: {} vs. {}.. !".format(i, o_shape, my_shape))
        # get result 
        scenario = plays[o_shape] 
        print(scenario)
        score = plays[o_shape][my_shape]
        total_score = total_score + shape_values[my_shape] + score
        i = i + 1 
    print(total_score)

if __name__ == '__main__':
    main()
