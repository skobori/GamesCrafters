import sys

"""
A simple solver for 4-to-1
"""

class Primitive:
    WIN, LOSS, TIE, DRAW, UNKNOWN = range(5)

PLAYER1, PLAYER2 = 0, 1

def primitive(pos):
    if pos == 0:
        return Primitive.LOSS
    else:
        return Primitive.UNKNOWN

def gen_moves(pos):
    if pos == 1:
        return [-1]
    else:
        return [-1, -2]

def do_move(pos, move):
    return pos + move

def solve_pos(pos):
    if primitive(pos) == Primitive.LOSS:
        return Primitive.LOSS
    moves = gen_moves(pos)
    new_positions = [pos + move for move in moves]
    for position in new_positions:
        if solve_pos(position) == Primitive.LOSS:
            return Primitive.WIN
    return Primitive.LOSS

if __name__ == "__main__":
    if sys.argv == 1:
        initial_position = 4
    else:
        initial_position = int(sys.argv[1])
    sol = solve_pos(initial_position)
    if sol == Primitive.WIN:
        print "This is a winning position"
    elif sol == Primitive.LOSS:
        print "This is a losing position"