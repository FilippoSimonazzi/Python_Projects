from matplotlib import pyplot as plt

def get_sequence(sequence):
    new_sequence = []
    for i in range(len(sequence)):
        new_sequence.append(sequence[i])
        new_sequence.append(0)

    new_sequence = new_sequence[:-1]
    for i in range(len(new_sequence)):
        if new_sequence[i] == 0:
            new_sequence[i] = new_sequence[i-1] + new_sequence[i+1]

    return new_sequence

def get_points(n_steps):
    n = 0

    final_sequence = [1]
    sequence = [1,2,1]
    while n <= n_steps:
        if n == 0:
            initial_sequence = get_sequence([1,1])
            final_sequence += initial_sequence[:-1]
        else:
            sequence = get_sequence(sequence)
            final_sequence += sequence[:-1]
        n += 1

    return final_sequence

def plot_graph(n_steps):
    y_axis = get_points(n_steps)
    x_axis = [x for x in range(len(y_axis))]

    plt.scatter(x_axis, y_axis,
                s=1, c='black')
    plt.show()
    return y_axis

n = input('How many points to you want to consider? > ')
plot_graph(int(n))