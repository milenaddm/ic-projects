import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


class linear_regression(object):
    def __init__(self, maxepocas) -> None:
        super().__init__()

        self.x = pd.Series()
        self.y = pd.Series()
        self.t0 = 0    # theta 0
        self.t1 = 0    # theta 1
        self.maxepocas = maxepocas
        self.learning_rate = 0.01

    def run(self):
        self.read_data()
        self.init()

        plt.plot(self.x, self.y, 'o', label='y', color='orange')
        plt.title(f'Lucro por População')
        plt.legend()
        plt.ylabel("Lucro em $10.000s")
        plt.xlabel("População em 10.000s")
        plt.show()

        cost_arr = []

        for epoca in range(self.maxepocas):
            cost = self.update()
            cost_arr.append(cost)

        self.plot(cost_arr)

    def init(self):
        self.t0 = np.random.rand()
        self.t1 = np.random.rand()

    def read_data(self):
        data = pd.read_csv(
            './linear-regression/data/data1.txt', names=['x', 'y'])
        self.x = data['x']
        self.y = data['y']

    def cost(self):
        cost = 0

        for i in range(len(self.x)):
            h = self.t0 + self.t1 * self.x[i]
            cost = cost + math.pow((h - self.y[i]), 2)

        return cost / (2 * len(self.x))

    def error_0(self):
        error = 0

        for i in range(len(self.x)):
            h = self.t0 + self.t1 * self.x[i]
            error = error + (h - self.y[i])

        return error / len(self.x)

    def error_1(self):
        error = 0

        for i in range(len(self.x)):
            h = self.t0 + self.t1 * self.x[i]
            dif = (h - self.y[i])
            error = error + (dif * self.x[i])

        return error / len(self.x)

    def update(self):
        cost = self.cost()

        error_0 = self.error_0()
        error_1 = self.error_1()

        self.t0 = self.t0 - self.learning_rate * error_0
        self.t1 = self.t1 - self.learning_rate * error_1

        return cost

    def plot(self, cost):
        plt.plot(range(self.maxepocas), cost, label='cost', color='red')

        plt.title(f'Custo em relação ao número de iterações')
        plt.ylabel("Custo")
        plt.xlabel("Número de iterações")
        plt.show()

        hx = self.t0 + self.t1 * self.x

        plt.plot(self.x, hx, label='ajuste')
        plt.plot(self.x, self.y, 'o', label='lucro')

        plt.title(
            f'Ajuste Linear \n Número de epocas: {self.maxepocas}  Custo final: {cost[len(cost) - 1]}')
        plt.legend()
        plt.ylabel("Lucro em $10.000s")
        plt.xlabel("População em 10.000s")
        plt.show()
