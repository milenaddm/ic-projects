import sys
from getopt import getopt
import numpy as np

from fuzzy_tsk.fuzzy_tsk import fuzzy


def print_usage():
    print("fuzzy-tsk usage:\n\npython fuzzy-tsk -p <popsize> -m <mutation-rate>")


def parse_opts(opts):
    popsize = None
    mutation_rate = None

    # for i in range(0, len(opts)):
    #     if opts[i][0] == "-h":
    #         print_usage()
    #         exit()
    #     elif opts[i][0] == "-p":
    #         popsize = int(opts[i][1])
    #         if popsize % 2 != 0:
    #             print("Error!")
    #             print("Population must be even size!")
    #             exit()
    #     elif opts[i][0] == "-m":
    #         mutation_rate = float(opts[i][1][1:])

    # if not (popsize and mutation_rate):
    #     print("Bad usage!")
    #     print_usage()
    #     exit()

    return popsize, mutation_rate


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], ["hp:m:"], ["m="])
    popsize, mutation_rate = parse_opts(opts)

    algoritmo = fuzzy()

    algoritmo.run()

    print('OK')
