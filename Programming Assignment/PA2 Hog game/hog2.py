"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    all_dice = [dice() for _ in range(num_rolls)]
    return 1 if 1 in all_dice else sum(all_dice)
    # END PROBLEM 1


def piggy_points(score):
    """Return the points scored from rolling 0 dice.

    score:  The opponent's current score.
    """
    # BEGIN PROBLEM 2
    power = score ** 2
    lowest = power % 10
    while power:
        low = power % 10
        power //= 10
        if low < lowest:
            lowest = low
    return lowest + 3
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 in the case
    of a player using Piggy Points.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < goal, 'The game should be over.'
    # BEGIN PROBLEM 3
    return roll_dice(num_rolls, dice) if num_rolls else piggy_points(opponent_score)
    # END PROBLEM 3


def more_boar(player_score, opponent_score):
    """Return whether the player gets an extra turn.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> more_boar(21, 43)
    True
    >>> more_boar(22, 43)
    True
    >>> more_boar(43, 21)
    False
    >>> more_boar(12, 12)
    False
    >>> more_boar(7, 8)
    False
    """
    # BEGIN PROBLEM 4
    player = f'0{player_score}' if player_score < 10 else str(player_score)
    opponent = f'0{opponent_score}' if opponent_score < 10 else str(opponent_score)
    # return player[0] < opponent[0] and player[1] < opponent[1]
    return False
    # END PROBLEM 4


def next_player(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> next_player(0)
    1
    >>> next_player(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while score0 < goal and score1 < goal:
        if who:
            score1 += take_turn(strategy1(score1, score0), score0, dice, goal)
        else:
            score0 += take_turn(strategy0(score0, score1), score1, dice, goal)
        if not more_boar(eval(f"score{who}"), eval(f"score{next_player(who)}")):
            who = next_player(who)
        # END PROBLEM 5
        # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
        # BEGIN PROBLEM 6
        say = say(score0, score1)
        # END PROBLEM 6
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """

    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader is not None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)

    return say


def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """

    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))

    return say


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    Player 1 has reached a new maximum point gain. 9 point(s)!
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    Player 1 has reached a new maximum point gain. 21 point(s)!
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    Player 1 has reached a new maximum point gain. 30 point(s)!
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'

    # BEGIN PROBLEM 7
    def say(score0, score1):
        score = score1 if who else score0
        best_gain = running_high
        gain = score - last_score
        if gain > running_high:
            best_gain = gain
            print(f"Player {who} has reached a new maximum point gain. {best_gain} point(s)!")
        return announce_highest(who, score, best_gain)

    return say
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """

    def strategy(score, opponent_score):
        return n

    return strategy


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
    """

    # BEGIN PROBLEM 8
    def average(*args):
        all_dice = [original_function(*args) for _ in range(trials_count)]
        return sum(all_dice) / len(all_dice)

    # END PROBLEM 8
    return average


def max_scoring_num_rolls(dice=six_sided, trials_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    dic = {make_averaged(roll_dice, trials_count)(i, dice): i for i in range(1, 11)}
    return dic[max(dic.keys())]

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    baseline = strat_will
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    print(f"will strategy: {make_averaged(average_win_rate, 100)(strat_will)}")
    # print(f"will2 strategy: {make_averaged(average_win_rate, 100)(strat_will2)}")
    print(f"god strategy: {make_averaged(average_win_rate, 100)(strat_god)}")
    print(f"ryu strategy: {make_averaged(average_win_rate, 100)(strat_ryu)}")
    print(f"save strategy: {make_averaged(average_win_rate, 100)(strat_save)}")
    print(f"proud strategy: {make_averaged(average_win_rate, 100)(strat_proud)}")
    print(f"punn strategy: {make_averaged(average_win_rate, 10)(strat_punn)}")


def piggypoints_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10

    return num_rolls if piggy_points(opponent_score) < cutoff else 0
    # END PROBLEM 10


def more_boar_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    more_trig = more_boar(piggy_points(opponent_score) + score, opponent_score)
    return 0 if more_trig else piggypoints_strategy(score, opponent_score, cutoff, num_rolls)
    # END PROBLEM 11


#############################################################################
def final_strategy(score, opponent_score):
    """This strategy is improved from more boar strategy.
    and use all suggestion
    """
    # BEGIN PROBLEM 12
    num_rolls = 8 if score <= 90 else 3
    cutoff = 8
    return piggypoints_strategy(score, opponent_score, cutoff, num_rolls)
    # END PROBLEM 12


# test other strategy

def strat_001(score, opponent_score):
    num_rolls = 8
    cutoff = 15
    if score > 90:
        num_rolls = 3
    if score > 80 and opponent_score < 70:
        cutoff = 7
    return more_boar_strategy(score, opponent_score, cutoff, num_rolls)


def strat_002(score, opponent_score):
    num_rolls = 8
    cutoff = 15
    if score > 90:
        num_rolls = 3
    if score > 80 > opponent_score:
        cutoff = 6
    return more_boar_strategy(score, opponent_score, cutoff, num_rolls)


#############################################################################

def strat_ryu(score, opponent_score):
    if (score + opponent_score) % 7 == 0:
        rolls = 4
    else:
        rolls = 6
    return piggypoints_strategy(score, opponent_score, cutoff=8, num_rolls=rolls)


def roll_without_1(times, roll):
    y = 0
    result = 0
    while y < times:
        current_roll = roll()
        if current_roll != 1:
            result += current_roll
            y += 1
        return result


def strat_punn(score, opponent_score, dice=six_sided):
    """Write a brief description of your final strategy.

    ***
    Basically, this strategy chooses returns number based on your and your opponent's points.

    Statistics (for six sided dice):
    probability (no 1) = [ 0.83,  0.69,  0.57,  0.48,  0.40,  0.33,  0.28,  0.23,  0.19,  0.16]
    average points     = [~3.50, ~5.84, ~7.33, ~8.24, ~8.70, ~8.71, ~8.54, ~8.20, ~7.77, ~7.30]
    ***
    """
    # BEGIN PROBLEM 12
    my_win = GOAL_SCORE - score
    their_win = GOAL_SCORE - opponent_score
    roll = dice
    base_roll = 5

    if piggy_points(opponent_score) >= my_win or \
            (piggypoints_strategy(score, opponent_score, cutoff=9) == 0 and my_win <= 15):
        return 0
    if my_win > 50:
        if their_win > 50:
            return base_roll
        return base_roll + 2

    for roll_times in range(1, 8):
        passed_threshold = 0
        for i in range(100):
            total = roll_without_1(roll_times, roll)
            if total >= my_win:
                passed_threshold += 1
        if passed_threshold >= 45:
            return roll_times
    return base_roll


def strat_will(score, opponent_score):
    if score >= 97:
        return 0

        # more win condition
    if 100 - score < 13:
        return 3

        # more win condition
    if 100 - score < 17:
        return 4

        # always roll 6
    return 6


# def strat_will2(score, opponent_score):
#     lst_square_nine = [3]  # list of square that have nine in it

#     # get win cond with piggy if opponent score squared have nine
#     if score >= 91 and opponent_score in lst_square_nine:
#         return 0

#     # if score and opponent score in same range gain advantage and free 9pts by piggy_points
#     if opponent_score in lst_square_nine and score > opponent_score > 80 and score - opponent_score > 10:
#         return 0

#     # surely win if score == 97
#     if score >= 97:
#         return 0

#     # more win condition
#     if 100 - score < 17:
#         return 4

#     # always roll 6
#     return 6


def strat_god(score, opponent_score, goal=GOAL_SCORE):
    diff = goal - score
    num_roll = 4 if diff < 17 else 7

    return more_boar_strategy(score, opponent_score, num_rolls=num_roll)


def strat_save(score, opponent_score):
    cutoff = 8
    num_rolls = 8
    if score >= 85 and score > opponent_score:
        return 3
    return piggypoints_strategy(score, opponent_score, cutoff, num_rolls)


def strat_proud(score, opponent_score):
    num_rolls = 8
    cutoff = 15
    if score > 90:
        num_rolls = 3
    if score > 80 and opponent_score < 70:
        cutoff = 7
    return more_boar_strategy(score, opponent_score, cutoff, num_rolls)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()


if __name__ == '__main__':
    run_experiments()
    # dict_ = {key: [] for key in range(0, 10)}
    # for i in range(1, 101):
    #     minn = int(min(str(i ** 2)))
    #     dict_[minn].append(i)
    # for a, b in dict_.items():
    #     print(f"{a}  ({len(b)})   : ", *b)
