import numpy as np


class normal_equation(object):
    def load_X_and_Y(self):
        data = np.genfromtxt('./normal-equation/data/data2.txt', delimiter=',')
        X = data[:, :-1]
        Y = data[:, -1]

        return X, Y

    def evaluate_normal_equation(self, X, Y):
        by_transpose = np.matmul(np.transpose(X), X)
        by_transpose_inverse = np.linalg.inv(by_transpose)
        almost_done = np.matmul(by_transpose_inverse, np.transpose(X))
        return np.matmul(almost_done, Y)

    def run(self):
        X, Y = self.load_X_and_Y()
        Theta = self.evaluate_normal_equation(X, Y)

        return Theta[0], Theta[1]
