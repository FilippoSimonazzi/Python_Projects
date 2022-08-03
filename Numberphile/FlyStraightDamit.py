from matplotlib import pyplot as plt
from math import gcd

def get_next(idx, prev, y_axis):
    if gcd(idx, prev) == 1:
        next = prev + idx + 1
        y_axis.append(next)
    else:
        next = int(prev/gcd(idx, prev))
        y_axis.append(next)
    return y_axis

def plot_graph(n):
    x_axis = [x for x in range(n)]
    y_axis = [1, 1]

    for idx in range(2, n):
        y_axis = get_next(idx, y_axis[-1], y_axis)

    plt.scatter(x_axis, y_axis,
                s=1, c='black')
    plt.show()
    return y_axis

n = input('How many points to you want to consider? > ')
plot_graph(int(n))

#y_axis = plot_graph(1000)
#print(y_axis[636], y_axis[637], y_axis[638], y_axis[639], y_axis[640], y_axis[641], y_axis[642], y_axis[643])

#print(y_axis)
