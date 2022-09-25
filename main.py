from simulator import Simulator
from loader import loadBanner
import sys


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


def str2bool(v):
    if type(v) == bool:
        return v

    return v.lower() in ('true', '0')


argL = len(sys.argv)
data = []

try:
    simulation = int(sys.argv[argL - 1])
    guarantee = str2bool(sys.argv[argL - 5])
    pity = int(sys.argv[argL - 4])
    wishs = int(sys.argv[argL - 3])
    banner = str(sys.argv[argL - 2])
except Exception:
    simulation = int(input("Simulation(s): "))
    guarantee = str2bool(input("Guarantee: "))
    pity = int(input("Pity: "))
    wishs = int(input("Wish(s): "))
    banner = str(input("Banner: "))

print("Starting " + str(simulation) + " simulation of " + str(wishs) + " wish(s) with guarantee = " + str(guarantee) + ", pity = " + str(pity) + " and banner: " + banner)

for i in range(simulation):
    sim = Simulator(guarantee, pity, loadBanner(banner))
    data.append(start(sim, wishs))

analize(data)

