import numpy as np
import pandas as pd
import csv
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

        plt.plot(self.x, self.y, 'o', label='y')
        plt.title(f'Data')
        plt.legend()
        plt.show()

        error_0 = 0
        error_1 = 0

        for epoca in range(self.maxepocas):
            error_0, error_1 = self.update(epoca)
            # print(f't0: {self.t0} \t t1: {self.t1}')
            # self.plot(epoca, error_0, error_1)
        self.plot(self.maxepocas, error_0, error_1)

    def init(self):
        self.t0 = np.random.rand()
        self.t1 = np.random.rand()
        # print(f't0: {self.t0} \t t1: {self.t1}')


    def read_data(self):
        data = pd.read_csv('./linear-regression/data/data1.txt', names=['x', 'y'])
        # print(data)
        self.x = data['x']
        self.y = data['y']


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

    def update(self, epoca):

        error_0 = self.error_0()
        # print(f'Error 0: {error_0}')

        error_1 = self.error_1()
        # print(f'Error 1: {error_1}')


        self.t0 = self.t0 - self.learning_rate * error_0
        self.t1 = self.t1 - self.learning_rate * error_1
       
        return error_0, error_1


    def plot(self, epoca, error_0, error_1):

        hx = self.t0 + self.t1 * self.x

        plt.plot(self.x, hx, label='hx')
        plt.plot(self.x, self.y, 'o', label='y')


        plt.title(f'Epoch: {epoca}\nError 0: {error_0}\nError 1: {error_1}')
        plt.legend()
        plt.show()
