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

        self.init(3)
        self.plot(x_values)


        for i in range(100):
            # a = 0.01
            self.update(x_values, 0.1)
        self.plot(x_values)


    def init(self, limit):
        self.x_1  = np.random.rand()*limit
        self.x_2  = np.random.rand()*limit
        self.sig1 = np.random.rand()*limit
        self.sig2 = np.random.rand()*limit
        self.p1   = np.random.rand()*limit
        self.p2   = np.random.rand()*limit
        self.q1   = np.random.rand()*limit
        self.q2   = np.random.rand()*limit

    def plot(self, x_values):
        print(self.error(x_values))

        plt.plot(x_values, self.w1(x_values))
        plt.plot(x_values, self.w2(x_values))

        plt.plot(x_values, self.x_power_2(x_values))

        plt.show()

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

    def error(self, x_values):
        error = 0
        for x in x_values:
            error = error + (1/2)*np.power((self.y(x_values) - self.x_power_2(x_values)), 2)
        return error / len(x_values)

    def update(self, x, a):

        # Calculate error's derivatives
        e_p1 = (self.y(x) - self.x_power_2(x)) * (self.w1(x)/(self.w1(x) + self.w2(x))) * x

        e_p2 = (self.y(x) - self.x_power_2(x)) * (self.w2(x)/(self.w1(x) + self.w2(x))) * x

        e_q1 = (self.y(x) - self.x_power_2(x)) * (self.w1(x)/(self.w1(x) + self.w2(x)))

        e_q2 = (self.y(x) - self.x_power_2(x)) * (self.w2(x)/(self.w1(x) + self.w2(x)))

        e_x_1 = (self.y(x) - self.x_power_2(x)) * self.w2(x) * ((self.y1(x) - self.y2(x))/np.power((self.w1(x) + self.w2(x)), 2)) * self.w1(x) * ((x - self.x_1)/np.power(self.sig1, 2))

        e_x_2 = (self.y(x) - self.x_power_2(x)) * self.w1(x) * ((self.y2(x) - self.y1(x))/np.power((self.w1(x) + self.w2(x)), 2)) * self.w2(x) * ((x - self.x_2)/np.power(self.sig2, 2))

        e_sig1 = (self.y(x) - self.x_power_2(x)) * self.w2(x) * ((self.y1(x) - self.y2(x))/np.power((self.w1(x) + self.w2(x)), 2)) * self.w1(x) * (np.power((x - self.x_1), 2)/np.power(self.sig1, 3))

        e_sig2 = (self.y(x) - self.x_power_2(x)) * self.w1(x) * ((self.y1(x) - self.y2(x))/np.power((self.w1(x) + self.w2(x)), 2)) * self.w2(x) * (np.power((x - self.x_2), 2)/np.power(self.sig2, 3))

        # Update parameters
        self.p1 = self.p1 - (a * e_p1)
        self.p2 = self.p2 - (a * e_p2)
        self.q1 = self.q1 - (a * e_q1)
        self.q2 = self.q2 - (a * e_q2)
        self.x_1 = self.x_1 - (a * e_x_1)
        self.x_2 = self.x_2 - (a * e_x_2)
        self.sig1 = self.sig1 - (a * e_sig1)
        self.sig2 = self.sig2 - (a * e_sig2)
