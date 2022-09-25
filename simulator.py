from banner import *


class Simulator:

    def __init__(self, guarantee, pity, banner):
        self.__guarantee = guarantee
        self.__pity = pity
        self.__banner = banner

    def start(self, wishs):
        ws = []

        for i in range(wishs):
            w = self.__wish()
            ws.append(w)


        return ws

    def __wish(self):
        rand = self.__rand()

        self.__pity += 1

        four = 51
        five = 6

        if self.__pity % 10 == 0:
            four = 940

        if self.__pity > 75:
            five = self.__five()

        if rand < five:
            self.__pity = 0
            if self.__guarantee or randint(0, 1) == 1:
                self.__guarantee = False
                return self.__banner.getUpFiveStar(), 5
            else:
                self.__guarantee = True
                return self.__banner.getFiveStar(), 5

        if rand < four:
            return self.__banner.getUpFourStar(), 4

        return self.__banner.getThreeStar(), 3


    def __rand(self):
        """returns random number between 0 and 999"""
        return randint(0, 1000)

    def __five(self):
        """calculate hard pity"""
        return 99.4 * self.__pity - 7449

    def getPity(self):
        """get your pity"""
        return self.__pity

    def getBanner(self):
        return self.__banner
