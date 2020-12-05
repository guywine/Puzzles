import matplotlib.pyplot as plt
import sympy
import random
import pandas as pd 

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
    primes_gen = sympy.primerange(1, nth_prime + 1)
    primes_lst = [num for num in primes_gen]

    return primes_lst

def random_partition(l:list, p:int):
    '''
    Randomly partitions list to p equal length lists
    '''
    random.shuffle(l)
    return [l[i::p] for i in range(p)]

def random_partition_range(start: int, end:int, p:int, sort:bool=False):
    l = list(range(start,end+1))
    list_of_lists = random_partition(l, p)
    if sort:
        for l in list_of_lists:
            l.sort()
    return list_of_lists


if __name__=='__main__':
    l = list(range(1,121))
    # a = random_partition(l,4)
    [a,b,c,d] = random_partition_range(1,120,4, sort = True)
    list_of_lists = random_partition_range(1,120,4, sort = False)

    cond_df = pd.DataFrame({'pgl-1 his':a, 'pgl-1 cont.':b,'pgl-3 his':c, 'pgl-3 cont.':d})
    cond_df.to_csv('Guy_Itai_exp.csv')

