import random
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(lst):
    result = []
    for item in lst:
        inserted = False
        index = 0
        while not inserted and index < len(result):
            if item < result[index]:
                result.insert(index, item)
                inserted = True
            index += 1
        if not inserted:
            result.append(item)
    return result


def generate_list(size):
    lst = random.sample(range(1, 12501), size)
    return lst


def sort_comparison_chart():
    function = ("Insertion sort", "Merge sort")
    size = {
        '2500': (4.44, 101.61),
        '5000': (9.58, 413.50),
        '7500': (14.86, 937.14),
        '10000': (20.92, 1651.38),
        '12500': (26.45, 2576.65),
    }

    fig, ax = plt.subplots(layout='constrained')

    res = ax.grouped_bar(size, tick_labels=function, group_spacing=1)
    for container in res.bar_containers:
        ax.bar_label(container, padding=3)


    ax.set_ylabel('Time (ms)')
    ax.set_xlabel('Funktion')
    ax.legend(loc='upper left', frameon=False, ncols=5)
    ax.set_ylim(0,3000)
    plt.show()



sort_comparison_chart()