import csv
import random
from typing import List


def check_equal(l1: List[str], l2: List[str]):
    return len(l1) == len(l2) and sorted(l1) == sorted(l2)


if __name__ == '__main__':
    original = ['Ida', 'Malene', 'Rasmus', 'Mor', 'Far', 'Bettina', 'Michael', 'Jesper']
    givers = ['Ida', 'Malene', 'Rasmus', 'Mor', 'Far', 'Bettina', 'Michael', 'Jesper']
    receivers = []
    for index, person in enumerate(givers):
        rand_number = random.randint(0, len(original) - 1)
        while givers[index] == givers[rand_number]:
            rand_number = random.randint(0, len(original) - 1)
        receivers.append(original[rand_number])
        del original[rand_number]

    assert check_equal(givers, receivers)
    pairs = [x for x in zip(givers, receivers)]
    print(pairs)

    with open('julegaver.csv', 'w') as out:
        csv_out = csv.writer(out)
        for row in pairs:
            csv_out.writerow(row)
