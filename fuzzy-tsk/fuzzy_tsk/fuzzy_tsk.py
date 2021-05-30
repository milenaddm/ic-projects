import numpy as np
import math
import matplotlib as mp
import matplotlib.pyplot as plt


class fuzzy(object):
    def __init__(self) -> None:
        super().__init__()

        #tation_rate = mutation_rate

    def run(self):

        x_values = np.linspace(-2, 2, 100)

        self.tsk(x_values, lambda x: self.gaussian(x, -2, 1), lambda x: self.gaussian(x, 2, 1))



    def gaussian(self, x, mu, sigma):
        return np.exp(-np.power(x - mu, 2) / (2 * np.power(sigma, 2)))

    def x_power_2(self, x):
        return np.power(x, 2)

    def tsk(self, x_values, gaussian1, gaussian2):
        y_array = []
        p1 = 1
        p2 = 1
        q1 = 0
        q2 = 0


        for i, x in enumerate(x_values):
            y1 = p1 * x + q1 
            y2 = p2 * x + q2 

            w1 = gaussian1(x)
            w2 = gaussian2(x)

            print(i, x)
            print(y1)
            print(y2)
            print(w1)
            print(w2)
            print((w1 * y1 + w2 * y2)/(w1 + w2))
            print()

            y = (w1 * y1 + w2 * y2)/(w1 + w2)
            y_array.append(y)


        #plt.plot(x_values, gaussian1(x_values))
        #plt.plot(x_values, gaussian2(x_values))

        plt.plot(x_values, y_array)
        plt.plot(x_values, self.x_power_2(x_values))
        plt.show()


