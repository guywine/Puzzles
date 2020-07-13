import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from itertools import cycle
from typing import Tuple, List

# https://stackoverflow.com/questions/38965410/how-to-show-image-sequences-as-video-clip-on-python


def initiate_array():
    """
    Initiates 3*3 array with 1 in the middle.
    """
    arr = np.zeros((3, 3))
    arr[1, 1] = 1
    return arr


def inflate_array(arr: np.array):
    """
    Adds a layer off zeros to the borders of array.
    """
    dim = arr.shape[0]
    new_arr = np.zeros((dim + 2, dim + 2))
    new_arr[1:-1, 1:-1] = arr
    return new_arr


def next_step(a: np.array):
    """
    Takes an array and updates it by the rules of boxes.
    """
    a = inflate_array(a)
    cells_to_mark_list = find_boxes_with_one_neighbour(a)
    a = mark_cells_in_list(a, cells_to_mark_list)
    return a


def find_boxes_with_one_neighbour(a: np.array):
    """
    Check which empty (0 marked) boxes have only one friend (1 marked)
    """
    cells_to_mark_list = []  # list of tuples, (row,col)
    for row in range(a.shape[0]):
        for col in range(a.shape[1]):
            if a[row, col] == 0 and num_of_neighbours(a, (row, col)) == 1:
                cells_to_mark_list.append((row, col))
    return cells_to_mark_list


def num_of_neighbours(a: np.array, inds: Tuple[int, int]) -> int:
    """
    Gets an array of 1/0, and indices of a cell (that is '0')
    Returns the number of direct neighbor cells with '1' value.
    """
    row = inds[0]
    col = inds[1]
    assert a[row, col] == 0, "cell checked is not zero itself"

    num_of_ones = 0
    if row != 0:
        num_of_ones += a[row - 1, col]
    if row != a.shape[0] - 1:
        num_of_ones += a[row + 1, col]
    if col != 0:
        num_of_ones += a[row, col - 1]
    if col != a.shape[1] - 1:
        num_of_ones += a[row, col + 1]

    return int(num_of_ones)


def mark_cells_in_list(a: np.array, cell_lst: List[Tuple]):
    """
    Gets a list of tuples (row, col), marks them 1 in the array.
    """
    for cell in cell_lst:
        a[cell] = 1
    return a


def updatefig(*args):
    """
    Updates figure with new a
    """
    global a, i
    if not pause:
        a = next_step(a)
        im.set_array(a)
        i += 1
        i_text.set_text(i_template % i)
        if i > 7 and math.log2(i).is_integer():
            im.set_cmap(next(colors_pool))
    return (im, i_text)


def onClick(event):
    global pause
    pause ^= True


if __name__ == "__main__":
    a = initiate_array()

    #########################
    fig = plt.figure()
    pause = False

    colors = ['Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'Greys']
    colors_pool = cycle(colors)

    im = plt.imshow(a, cmap="Greys", animated=True)
    i = 1
    i_template = "i = %d"
    i_text = plt.text(-0.3, -0.3, "", fontsize=15)

    fig.canvas.mpl_connect("button_press_event", onClick)
    ani = animation.FuncAnimation(fig, updatefig, interval=200, blit=True)
    plt.show()
