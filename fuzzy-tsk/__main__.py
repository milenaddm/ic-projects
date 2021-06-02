import sys
from getopt import getopt
import numpy as np

from fuzzy_tsk.fuzzy_tsk import fuzzy


def print_usage():
    print("fuzzy-tsk usage:\n\npython fuzzy-tsk -n <number-of-points> -m <maxepocas> -l <learning-rate>")


def parse_opts(opts):
    n_points = None
    maxepocas = None
    learning_rate = None

    for i in range(0, len(opts)):
        if opts[i][0] == "-h":
            print_usage()
            exit()
        elif opts[i][0] == "-n":
            n_points = int(opts[i][1])
        elif opts[i][0] == "-m":
            maxepocas = int(opts[i][1])
        elif opts[i][0] == "-l":
            learning_rate = float(opts[i][1][1:])

    if not (n_points and maxepocas and learning_rate):
        print("Bad usage!")
        print_usage()
        exit()

    return n_points, maxepocas, learning_rate


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], "hn:m:l:")
    n_points, maxepocas, learning_rate = parse_opts(opts)

    algoritmo = fuzzy(n_points, maxepocas, learning_rate)

    algoritmo.run()
