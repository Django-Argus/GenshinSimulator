from objects import *
from banner import *
import json


def loadBanner(file):
    f = open(file)
    data = json.load(f)
    loadedData = loadObjects(data['load_path'])
    return Banner(data['name'], loadedData, loadUp(data['up'], loadedData))

def loadUp(ups, loadedData):
    u = []
    j = 0
    for i in ups:
        u.append([])
        for k in ups[i]:
            for l in loadedData[j]:
                if k == l.getName():
                   u[j].append(l)
        j += 1
    return u


def loadObjects(file):
    f = open(file)
    data = json.load(f)

    f.close()
    return __loadList(data['3*']), __loadList(data['4*']), __loadList(data['5*'])


def __loadList(data):
    l = []
    for i in data:
        type = WEAPON
        if i['type'] == 'character':
            type = CHARACTER
        l.append(Object(type, i['name']))

    return l
