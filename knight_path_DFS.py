from enum import Enum


class EnumeratedLetters(Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8


# class to represent each of 64 squares of the chess board
class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if 0 < self.x + other.x < 9 and 0 < self.y + other.y < 9:
            return Square(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if isinstance(other, Square):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False

    def __str__(self):
        return str(EnumeratedLetters(self.x).name) + str(self.y)


# priority of DFS as mentioned in the task
search_priority = [Square(1, 2),
                   Square(-1, 2),
                   Square(-2, 1),
                   Square(-2, -1),
                   Square(-1, -2),
                   Square(1, -2),
                   Square(2, -1),
                   Square(2, 1)]


# helper function to deal with str input
def convert_coordinates(coordinates):
    left = coordinates[0]
    right = coordinates[1]
    if left.isalpha():
        return EnumeratedLetters[left].value, int(right)
    else:
        return str(EnumeratedLetters(int(left)).name + right)


# implementation of additional methods to list type: withdraw() withdraws next element in MyStack() instance
class MyStack(list):
    def push(self, item):
        self.append(item)

    def withdraw(self):
        if len(self) != 0:
            return self[len(self) - 1]
        return None


# input handler
with open('in.txt') as file:
    knight_position = file.readline().strip()
    target_position = file.readline().strip()
    knight_x, knight_y = convert_coordinates(knight_position)
    target_x, target_y = convert_coordinates(target_position)
    start = Square(knight_x, knight_y)
    target = Square(target_x, target_y)
# print(target_x, target_y)
# print(target_position)


def get_illegal_squares(pawn_pos):
    square_1, square_2 = Square(pawn_pos.x - 1, pawn_pos.y - 1), Square(pawn_pos.x + 1, pawn_pos.y - 1)
    return square_1, square_2


stack = MyStack()
visited = [x for x in get_illegal_squares(target)]
visited.append(start)
stack.push(start)
while stack.withdraw() != target:
    current_square = stack.withdraw()
    for move in search_priority:
        next_move = current_square + move
        if next_move is not None and next_move not in visited:
            stack.push(next_move)
            visited.append(next_move)
            break
    # if stack.withdraw() == current_square:
    #     stack.pop()

prev = ''
for i in stack:
    prev += str(i) + '\n'
path = prev[:-1]
# print(path)

# output handler
with open('out.txt', 'w') as file:
    file.write(path)
