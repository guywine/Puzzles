import numpy as np
import matplotlib.pyplot as plt 

def what_I_need():

    wanted_mean = np.linspace(95, 99, num=50)
    grade_needed = []
    for i in range(50):
        needed_grade_i = (28 * wanted_mean[i] - 99.4 * 24)/4
        grade_needed.append(needed_grade_i)
    return grade_needed, wanted_mean

def plot_grades(grade_needed, wanted_mean):
    fig = plt.figure()
    plt.plot(grade_needed, wanted_mean)
    plt.xlabel('grade needed')
    plt.ylabel('mean final')
    plt.tight_layout()
    plt.grid()
    plt.show()

def compute_plot():
    grade_needed, wanted_mean = what_I_need()
    plot_grades(grade_needed, wanted_mean)

compute_plot()