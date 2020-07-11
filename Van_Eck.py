import matplotlib.pyplot as plt
import numpy as np
import helper_functions as hf

def create_seq(n: int):
    """
    Creates a list of Van Eck sequence, length n.
    Van Eck sequence:
    https://www.youtube.com/watch?v=etMJxB-igrc&feature=youtu.be
    """
    seq = [0, 0]
    found = {0}
    for i in range(1, n - 1):
        # print(f'working on {i} : {seq[i]}')
        if seq[i] in found:
            dist = find_dist_of_last(seq)
            # print(f'distance = {dist}')
            seq.append(dist)
        else:
            seq.append(0)
            found.add(seq[i])
    return seq


def find_dist_of_last(seq: list):
    """
    returns distance between last element of the list
    and the previous index he appeared in.
    """
    elem = seq[-1]
    for ind in reversed(range(len(seq)-1)):
        # print(f'index : {ind}')
        if seq[ind] == elem:
            # print(f'stopped here index {ind} element {seq[ind]}')
            last_ind = ind
            break
    dist = len(seq) - last_ind - 1
    return dist

    

if __name__ == "__main__":
    seq = create_seq(20_000)
    print(f'length: {len(seq)}')
    hf.plot_list(seq, head='Van Eck')

