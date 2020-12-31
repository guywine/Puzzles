import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


def compute_chances(chance: float):
    range_of_tests = range(30, 200)
    chance_of_finding = []
    for i in range_of_tests:
        chance_i = 1 - (1 - chance) ** i  # chance to have that many negatives
        chance_of_finding.append(chance_i)
    return list(range_of_tests), chance_of_finding


def plot_bernouli(test_range, chance_of_finding, chance: float):
    fig = plt.figure()
    plt.title(f"for a chance of {str(Fraction(chance))}")
    plt.plot(test_range, chance_of_finding)
    plt.xlabel("number of trials")
    plt.ylabel("chance of atleast one positive")
    plt.ylim(min(chance_of_finding) - 0.05, 1)
    xmin0 = test_range[0] - 3
    xmax0 = test_range[-1] + 3
    plt.xlim(xmin0, xmax0)
    plt.hlines(y=0.95, xmin=xmin0, xmax=xmax0, linestyles="dashed", label="98%")
    plt.tight_layout()
    plt.grid()
    plt.show()


def bernouli_tests(chance: float):
    range_of_tests, chance_of_positive = compute_chances(chance)
    plot_bernouli(range_of_tests, chance_of_positive, chance)

bernouli_tests(chance = 1 / 64)

