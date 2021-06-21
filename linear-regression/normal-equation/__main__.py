import numpy as np

from normal_equation.normal_equation import normal_equation


def print_usage():
    print("normal-equation usage:\n\npython normal-equation")


if __name__ == "__main__":
    algoritmo = normal_equation()
    a, b = algoritmo.run()

    print(f'Normal equation: {round(a, 2)} + {round(b, 2)}x')
