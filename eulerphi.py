import matplotlib.pyplot as plt
import numpy as np
from math import gcd


"""Script for playing with the Euler-phi function"""


def rel_prime(a, b):
    return gcd(a, b) == 1


def euler_phi(n):
    """
    Count the number of positive integers 1<m<n that are relatively prime with n
    :param n: variable (int)
    :return: (int)
    """

    integers = np.arange(2, n)
    count = 0
    for integ in integers:
        if rel_prime(integ, n):
            count += 1

    return count


# Let's play
cap = 10000   
x_values = np.arange(2, cap)
y_values = np.asarray([euler_phi(x) for x in x_values])

# print(x_values)
# print(y_values)

s = [0.01 for n in range(len(x_values))]
plt.scatter(x_values, y_values, s)
plt.show()
