import numpy as np
import pandas as pd
import csv
import math
import matplotlib.pyplot as plt


class linear_regression(object):
    def __init__(self, maxepocas, learning_rate) -> None:
        super().__init__()

        self.data = pd.DataFrame()
        self.x1 = pd.Series()
        self.x2 = pd.Series()
        self.y = pd.Series()
        self.t0 = 0    # theta 0
        self.t1 = 0    # theta 1
        self.t2 = 0    # theta 2
        self.maxepocas = maxepocas
        self.learning_rate = learning_rate

    def run(self):
        self.read_data()
        self.init()

        plt.plot(self.x1, self.y, 'o', label='size')
        plt.plot(self.x2, self.y, 'o', label='beds')
        plt.title(f'Data')
        plt.legend()
        plt.ylabel("Price")
        plt.xlabel("Feature")
        plt.show()

        self.normalize_data()

        plt.plot(self.x1, self.y, 'o', label='size')
        plt.plot(self.x2, self.y, 'o', label='beds')
        plt.title(f'Data')
        plt.legend()
        plt.ylabel("Price")
        plt.xlabel("Normalized feature")
        plt.show()

        cost_arr = []

        for epoca in range(self.maxepocas):
            cost = self.update()
            cost_arr.append(cost)
            # print(f't0: {self.t0} \t t1: {self.t1}')
            # self.plot(epoca, error_0, error_1)
        self.plot(cost_arr)

    def init(self):
        self.t0 = np.random.rand()
        self.t1 = np.random.rand()
        # print(f't0: {self.t0} \t t1: {self.t1}')


    def read_data(self):
        data = pd.read_csv('./linear-regression-multi-variables/data/data2.txt', names=['size', 'beds', 'price'])

        self.data = data
        self.x1 = data['size']
        self.x2 = data['beds']
        self.y = data['price']

    def normalize_data(self):
        # Media
        m1 = 0
        for x in self.x1:
            m1 = m1 + x
        m1 = m1 / len(self.x1)

        # Desvio padrao
        s1 = 0
        for x in self.x1:
            s1 = s1 + math.pow((x - m1), 2)
        s1 = s1 / len(self.x1)
        s1 = math.sqrt(s1)

        # Normalization
        x1 = []
        for x in self.x1:
            x1.append((x - m1)/ s1)
        self.x1 = pd.Series(x1)

        # Media
        m2 = 0
        for x in self.x2:
            m2 = m2 + x
        m2 = m2 / len(self.x2)

        # Desvio padrao
        s2 = 0
        for x in self.x2:
            s2 = s2 + math.pow((x - m2), 2)
        s2 = s2 / len(self.x2)
        s2 = math.sqrt(s2)

        # Normalization
        x2 = []
        for x in self.x2:
            x2.append((x - m2)/ s2)
        self.x2 = pd.Series(x2)


    def cost(self):
        cost = 0

        for i in range(len(self.y)):
            h = self.t0 + self.t1 * self.x1[i] + self.t2 * self.x2[i]
            cost = cost + math.pow((h - self.y[i]), 2)

        return cost / (2 * len(self.y))


    def error_0(self):
        error = 0

        for i in range(len(self.y)):
            h = self.t0 + self.t1 * self.x1[i] + self.t2 * self.x2[i]
            error = error + (h - self.y[i])

        return error / len(self.y)


    def error_x(self, x):
        error = 0

        for i in range(len(x)):
            h = self.t0 + self.t1 * self.x1[i] + self.t2 * self.x2[i]
            dif = (h - self.y[i])
            error = error + (dif * x[i])

        return error / len(x)

    def update(self):

        cost = self.cost()

        error_0 = self.error_0()
        error_1 = self.error_x(self.x1)
        error_2 = self.error_x(self.x2)


        self.t0 = self.t0 - self.learning_rate * error_0
        self.t1 = self.t1 - self.learning_rate * error_1
        self.t2 = self.t2 - self.learning_rate * error_2

        return cost


    def plot(self, cost):

        plt.plot(range(self.maxepocas), cost, label='cost', color='red')

        plt.title(f'Cost X number of iteractions \n Learning rate: {self.learning_rate}')
        plt.ylabel("Cost")
        plt.xlabel("Number of iteractions")
        plt.show()
