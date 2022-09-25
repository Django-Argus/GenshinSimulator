
class Object:

    def __init__(self, type, name):
        self.__type = type
        self.__name = name

    def __str__(self):
        return str(self.__type) + "@" + self.__name

    def __repr__(self):
        return str(self.__type) + "@" + self.__name

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type


class Type:

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name


WEAPON = Type("weapon")
CHARACTER = Type("character")
