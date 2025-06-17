"""
Maze Coin Hunt Game - Jr. DEEP Coding Sample Activity

This program simulates a simple 5x5 maze game where the player navigates the grid using
the directions 'N' (North), 'E' (East), 'S' (South), and 'W' (West). The player starts
at the top-left corner of the maze and must find 3 hidden coins randomly placed
throughout the maze.
"""
import random

# 1 dimensional list representing the 5x5 map for the maze
# [ 0,  1,  2,  3,  4,
#   5,  6,  7,  8,  9,
#  10, 11, 12, 13, 14,
#  15, 16, 17, 18, 19,
#  20, 21, 22, 23, 24 ]
maze = [""] * 25

# Place 3 coins at random unique positions
coin_positions = random.sample(range(1, 25), 1)
for pos in coin_positions:
    maze[pos] = "coin"
    print(pos)

player_pos = 0
items_found = 0
def move(direction, pos):
    row, col = divmod(pos, 5)
    if direction == "N" and row > 0:
        return pos - 5
    elif direction == "S" and row < 4:
        return pos + 5
    elif direction == "E" and col < 4:
        return pos + 1
    elif direction == "W" and col > 0:
        return pos - 1
    else:
        print("You can't go that way!")
        return pos


num_moves = 0

while items_found < 3:
    print(f"You are at position {player_pos}.")
    direction = input("Move (N/E/S/W): ").upper()

    if direction not in ["N", "E", "S", "W"]:
        print("Invalid direction.")
        continue

    new_pos = move(direction, player_pos)
    num_moves += 1
    if maze[new_pos] == "coin":
        print(f"You found a coin! This took you {num_moves} moves")
        items_found += 1
        maze[new_pos] = ""

    player_pos = new_pos

print("You found all 3 coins! You win!")
