class LevelControl(object):

    __aLevel = False

    def __init__(self, pLevel):
        self.__aLevel = pLevel

    def getLevel(self):
        return self.__aLevel

    def setLevel(self, pLevel):
        self.__aLevel = pLevel
