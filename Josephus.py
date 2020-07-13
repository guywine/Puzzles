import numpy as np
import matplotlib.pyplot as plt
import math

# https://www.youtube.com/watch?v=uCsD3ZGzMgE


def play(n: int, print_turns: bool = False):
    i = n - 1
    circle = np.ones((n,))
    turn = 1
    list_of_killed = []
    while int(np.sum(circle)) != 1:
        i = move_k_living(circle, i)
        circle[i] = 0  # kill
        list_of_killed.append(i + 1)
        if print_turns:
            print(f"turn {turn}, {circle}\t{i+1} killed")
        turn += 1
    winner = np.where(circle == 1)
    return int(winner[0]), list_of_killed


def move_k_living(circ_a: np.array, i: int, k_moves: int = 2):
    moved = 0
    while moved < k_moves:
        i += 1
        if circ_a[i % len(circ_a)] == 1:
            moved += 1
    return i % len(circ_a)


def print_first_of_each_round(players_list: list):
    firsts_indices = get_indices_of_firsts(players_list)
    firsts_list = [players_list[ind] for ind in firsts_indices]
    print(f"Firsts of rounds: {firsts_list}")


def get_indices_of_firsts(players_list: list):
    firsts_list = [0]
    for i in range(1, len(players_list)):
        if players_list[i] < players_list[i - 1]:
            firsts_list.append(i)
    return firsts_list


def print_diffs_of_each_round(players_list: list):
    diffs = get_diffs_of_each_round(players_list)
    print(f"Diffs of rounds: {diffs}")


def get_diffs_of_each_round(players_list: list):
    firsts_indices = get_indices_of_firsts(players_list)
    diffs = [
        players_list[firsts_indices[i] + 1] - players_list[firsts_indices[i]]
        for i in range(len(firsts_indices))
        if firsts_indices[i] + 1 < len(players_list)
    ]
    # last diff mught be negative since there are two 'firsts' in a row
    return diffs


def plot_winners(game_range: range):
    global winners
    plt.figure()
    plt.title("winners of game")
    plt.xlabel("number of players")
    plt.ylabel("number of winner")

    plt.scatter(list(game_range), winners, s=4)
    x_lines = [num for num in game_range if math.log2(num).is_integer()]
    plt.vlines(
        x_lines,
        ymin=0,
        ymax=max(winners),
        linestyles="dashed",
        label="x"
        )
    plt.show()


if __name__ == "__main__":
    winners = []
    game_range = range(1, 500)
    for n in game_range:
        winner_i, list_of_killed = play(n)
        winners.append(winner_i)
        print(f"{n} players\twinner:\tplayer {winner_i+1}")
        # print(f'Killed: {list_of_killed}')

        # print_first_of_each_round(list_of_killed)
        # print_diffs_of_each_round(list_of_killed)

    plot_winners(game_range)

    """
    Results:
    The differences increase each round in the power of 2:
    2, 4, 8, 16

    For even number of players:
    - 2, 3... and changing (1, or 5)
    """
