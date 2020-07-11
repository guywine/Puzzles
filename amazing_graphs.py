# https://www.youtube.com/watch?v=pAMgUB51XZA&feature=youtu.be

import helper_functions as hf


def fly_straight(n):
    """
    Creats list length n with values of this sequence
    """
    seq = [1, 1]
    for i in range(1, n - 1):
        gcd = find_gcd(seq[i], len(seq))
        if gcd == 1:  # if no common divisor
            seq.append(seq[i] + len(seq) + 1)
        else:
            seq.append(seq[i] / gcd)
    return seq


def find_gcd(a, b):
    """
    Returns the greates common divisor of two numbers.
    If there are no common divisors, returns 1.
    """
    if a == 0:
        return b
    if b == 0:
        return a

    q = a // b
    r = a - q * b

    gcd = find_gcd(b, r)

    return gcd


def prime_reverse(n: int):
    seq = []
    n_primes = hf.n_first_primes(n)
    for num in n_primes:
        res = subtract_reverse_binary(num)
        seq.append(res)
    return seq


def subtract_reverse_binary(num: int):
    """
    Finds reverse binary of number, and subtracts it from original
    """
    b_num = bin(num)
    rev_bin = b_num[-1:1:-1]  # removes the '0b' at beggining of string
    rev_bin_num = int(rev_bin, 2)
    return num - rev_bin_num


if __name__ == "__main__":
    fly_str = fly_straight(1_000)
    hf.plot_list(fly_str, head="fly straight", line_style="None")

    prime_revs = prime_reverse(12_000)
    hf.plot_list(prime_revs, head="prime reverse", line_style="None")
