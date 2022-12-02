f = open("input.txt", "r")
lines = f.readlines()

def f(lines):
    me = []
    opponents = []
    for line in lines:
        opponents.append(line[0])
        me.append(line[2])
    return me, opponents

def get_my_score(choices):
    score = 0
    for choice in choices:
        if choice == 'X':
            score = score + 1
        elif choice == 'Y':
            score = score + 2
        elif choice == 'Z':
            score = score + 3
    return score

def get_win_score(me, opponents):
    score = 0
    for i in range(len(me)):
        if (
                (me[i] == 'X' and opponents[i] == 'C') or
                (me[i] == 'Y' and opponents[i] == 'A') or
                (me[i] == 'Z' and opponents[i] == 'B')):
            score = score + 6

        elif (
                (me[i] == 'X' and opponents[i] == 'A') or
                (me[i] == 'Y' and opponents[i] == 'B') or
                (me[i] == 'Z' and opponents[i] == 'C')):
            score = score + 3

    return score

me, opponents = f(lines)

my_score = get_my_score(me)
win_score = get_win_score(me, opponents)

print(my_score + win_score)

#Part2

def get_win_play(play):
    if play == 'A':
        return 'Y'
    elif play == 'B':
        return 'Z'
    elif play == 'C':
        return 'X'

def get_loose_play(play):
    if play == 'A':
        return 'Z'
    elif play == 'B':
        return 'X'
    elif play == 'C':
        return 'Y'

def get_draw_play(play):
    if play == 'A':
        return 'X'
    elif play == 'B':
        return 'Y'
    elif play == 'C':
        return 'Z'

def get_my_choices(opponents, win_status):
    my_choices = []
    for i in range(len(opponents)):
        if win_status[i] == 'X':
            my_choices.append(get_loose_play(opponents[i]))
        elif win_status[i] == 'Y':
            my_choices.append(get_draw_play(opponents[i]))
        else:
            my_choices.append(get_win_play(opponents[i]))
    return my_choices

my_choices = get_my_choices(opponents, me)

my_score = get_my_score(my_choices)
win_score = get_win_score(my_choices, opponents)

print(my_score + win_score)