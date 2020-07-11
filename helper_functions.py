import matplotlib.pyplot as plt
import sympy
# from sympy import primerange, isprime


def plot_list(lst: list, head: str, line_style: str = "solid"):
    """
    Plots values of a list
    """
    fig, ax = plt.subplots()
    ax.plot(
        range(len(lst)),
        lst,
        linestyle=line_style,
        markersize="2",
        marker=".",
        color="darkcyan",
    )
    plt.title(head)
    ax.grid(axis="y")
    plt.show()


def n_first_primes(n):
    """
    Return first n prime numbers.
    """
    nth_prime = sympy.prime(n)
    primes_gen = sympy.primerange(1, nth_prime+1)
    primes_lst = [num for num in primes_gen]

    return primes_lst
