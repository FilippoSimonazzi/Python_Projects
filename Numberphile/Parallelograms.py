from matplotlib import pyplot as plt

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def get_num(n):
    bin1 = "{0:b}".format(n)
    bin2 = bin1[::-1]
    return n - int(bin2, 2)

def plot_graph(tot):
    x_axis = primes(tot)
    y_axis = []

    for n in x_axis:
        y_axis.append(get_num(n))

    plt.scatter(x_axis, y_axis,
                s=1, c='black')
    plt.show()
    return y_axis

n = input('How many points to you want to consider? > ')
plot_graph(int(n))

