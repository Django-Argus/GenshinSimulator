from random import randint, choice


class Banner:

    def __init__(self, name, lists, ups):
        """init banner with fiveStar (str) and other (tuple[3])"""
        j = 0
        for i in ups:
            for k in i:
                for l in lists[j]:
                    if k == l:
                        lists[j].remove(l)
            j += 1

        self.__lists = lists
        self.__ups = ups

    def getFivesStar(self):
        return self.__getUps(2)

    def getFoursStar(self):
        return self.__getUps(1)

    def getThreesStar(self):
        return self.__getUps(0)

    def __getUps(self, i):
        if len(self.__ups) > 0:
            return self.__ups[i]

    def getUpFiveStar(self):
        five = self.getFivesStar()
        if len(five) > 0:
            return choice(five)

    def getUpFourStar(self):
        four = self.getFoursStar()
        return four[randint(0, len(four) - 1)]

    def getUpThreeStar(self):
        three = self.getFoursStar()
        return three[randint(0, len(three))]

    def getThreeStar(self):
        return self.__getChoice(0)

    def getFourStar(self):
        return self.__getChoice(1)

    def getFiveStar(self):
        return self.__getChoice(2)

    def __getChoice(self, i):
        if len(self.__lists[i]) > 0:
            return choice(self.__lists[i])
