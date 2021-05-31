import numpy as np
import math
import matplotlib as mp
import matplotlib.pyplot as plt


class fuzzy(object):
    def __init__(self) -> None:
        super().__init__()

        #tation_rate = mutation_rate

    def run(self):

        x_values = np.linspace(-2, 2, 120)

        self.init()
        print(self.error(x_values))

        plt.plot(x_values, self.w1(x_values))
        plt.plot(x_values, self.w2(x_values))

        plt.plot(x_values, self.y(x_values))

        plt.show()

        self.init()
        print(self.error(x_values))

        plt.plot(x_values, self.w1(x_values))
        plt.plot(x_values, self.w2(x_values))

        plt.plot(x_values, self.y(x_values))

        plt.show()


    def init(self):
        self.x_1  = np.random.rand()*5
        self.x_2  = np.random.rand()*5
        self.sig1 = np.random.rand()*5
        self.sig2 = np.random.rand()*5
        self.p1   = np.random.rand()*5
        self.p2   = np.random.rand()*5
        self.q1   = np.random.rand()*5
        self.q2   = np.random.rand()*5


    def gaussian(self, x, x_, sigma):
        return np.exp(-np.power(x - x_, 2) / (2 * np.power(sigma, 2)))

    def x_power_2(self, x):
        return np.power(x, 2)

    def w1(self, x):
        return self.gaussian(x, self.x_1, self.sig1)

    def w2(self, x):
        return self.gaussian(x, self.x_2, self.sig2)

    def y1(self, x):
        return self.p1 * x + self.q1

    def y2(self, x):
        return self.p2 * x + self.q2

    def y(self, x):
        return (self.w1(x) * self.y1(x) + self.w2(x) * self.y2(x)) / (self.w1(x) + self.w2(x))

    def yd(self, x):
        # TODO: finish y derivative
        return (x)

    def error(self, x_values):
        error = 0
        for x in x_values:
            error = error + (1/2)*np.power((self.y(x_values) - self.yd(x_values)), 2)
        return error / len(x_values)

