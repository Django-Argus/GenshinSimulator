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


argL = len(sys.argv)
data = []
for i in range(sys.argv[argL - 1]):
    sim = Simulator(sys.argv[argL - 5], sys.argv[argL - 4], loadBanner(sys.argv[argL - 2]))
    data.append(start(sim, sys.argv[argL - 3]))

analize(data)

