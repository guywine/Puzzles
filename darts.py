"""
https://youtu.be/6_yU9eJ0NxA
uniform random darts throw, each throw decreases radius of target
"""

import random as rand
import statistics
import matplotlib.pyplot as plt
import numpy as np


def define_params():
    r0 = 1
    shape = "square"
    return r0, shape


def random_h(r0: float):
    x, y = random_xy(r0)
    h = (x ** 2 + y ** 2) ** 0.5
    return h


def random_xy(r0: float):
    x = rand.uniform(-r0, r0)
    y = rand.uniform(-r0, r0)
    return x, y


def dart_h(r0: float, shape: str = "square"):
    h = random_h(r0)
    if shape == "square":
        return h
    else:  # if shape is circle
        while h > r0:  # only darts within r0 circle are allowed
            # print(f'h to big : {h}')
            h = random_h(r0)
        return h


def plot_h_dist(n: int = 1000, shape="circle"):
    hs = []
    r0 = 1
    for i in range(n):
        hs.append(dart_h(r0, shape))

    plt.figure(1)
    bin_values, _, _ = plt.hist(hs, bins=100)
    y_max = max(bin_values)
    plt.text(0.05, y_max*0.95, f'mean={np.mean(hs):.5f}')
    plt.xlim(left=0)
    plt.title('Distribution of distance from center')
    plt.xlabel("h (dist from center)")
    plt.ylabel('number of appearances')
    plt.show()


def update_radius(r_prev: float, h: float):
    return (r_prev ** 2 - h ** 2) ** 0.5


def play_game(r0: float, shape: str):
    r_current = r0
    score = 1
    h = dart_h(r0, shape)

    while h < r_current:
        # print(f'\nh : {h:.2f},\nr = {r_current:.2f}')
        score += 1
        r_current = update_radius(r_current, h)
        h = dart_h(r0, shape)

    # print(f'\nlast turn\nh : {h:.2f},\nr = {r_current:.2f}')
    return score


def display_results(scores: list, shape: str):
    mean = sum(scores) / len(scores)
    std = statistics.pstdev(scores)
    print(f"{shape}: Average = {mean}\tstd = {std:.5f}\n")


def play_many(r0: float, shape: str, n: int):
    scores = []
    for i in range(i_games):
        score = play_game(r0, shape)
        scores.append(score)
    return scores


def play_squares_and_circles(r0, i_games: int):
    print(f'Playing {i_games} games, with r0 : {r0}\n')

    scores_square = play_many(r0, 'square', i_games)
    display_results(scores_square, 'square')

    scores_circle = play_many(r0, 'circle', i_games)
    display_results(scores_circle, 'circle')

if __name__ == "__main__":
    r0 = 100
    i_games = 1_000_000

    # play_squares_and_circles(r0, i_games)

    plot_h_dist(10_000_000, shape='circle')

    """
    results:
    square: Average = 2.194      std = 0.91
    circle: Average = 2.718      std = 0.88
    """
