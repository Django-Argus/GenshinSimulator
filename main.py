from simulator import Simulator
from loader import loadBanner
import sys

p = 0

def start(sim, wishs):
    data = sim.start(wishs)

    length = len(data)
    list3 = []
    list4 = []
    list5 = []
    for i in data:
        if i[1] == 5:
            list5.append(i)
        elif i[1] == 4:
            list4.append(i)
        else:
            list3.append(i)

    len3 = len(list3)
    len4 = len(list4)
    len5 = len(list5)
    upFive = 0

    for i in list5:
        if i[0] in sim.getBanner().getFivesStar():
            upFive += 1

    return data, list3, list4, list5, upFive


def analize(data):
    wishs = len(data)
    upFive = 0
    for d in data:
        upFive += d[4] > 0

    print(str((upFive / wishs) * 100) + "%")


data = []
for i in range(10000):
    sim = Simulator(False, 9, loadBanner(sys.argv[-1]))
    data.append(start(sim, 147))

analize(data)

