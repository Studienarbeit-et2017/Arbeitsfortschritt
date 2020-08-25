import time

from PlantSensor import PlantSensor

class Plant (object):
    __aID = 0
    __aHumidity = 0.0
    __aTempratur = 0.0
    __aLight =0.0
    __aName = ""
    __aTime = 0.0
    __aWater = 0
    __aMacAddress = ""
    __aPlantSensor = PlantSensor(0)
    __aPlantFinsih = False

    def __init__(self, pID, pName):
        self.__aID = pID
        self.__aName = pName

    def newPlant(self, pID, pName, pTime, pWater, pMACSensor):
        self.__aID = pID
        self.__aName = pName
        self.__aTime = pTime
        self.__aWater = pWater
        self.__aMacAdresse =  pMACSensor
        self.__aPlantSensor = PlantSensor(pMACSensor)
        self.__aPlantFinsih = False

    def getName(self):
        return self.__aName

    def getID(self):
        return self.__aID

    def changeTime(self, pTime):
        self.__aTime = self.__aTime - pTime

        if self.__aTime <= 0:
            self.__aPlantFinsih = True

    def getTime(self):
        return self.__aTime

    def getWater(self):
        return self.__aWater

    def getLight(self):
        return self.__aPlantSensor.getLight()

    def getHumidity(self):
        return self.__aPlantSensor.getHumidity()

    def getTemperature(self):
        return self.__aPlantSensor.getTemperature()

    def getBatteryLevel(self):
        return self.__aPlantSensor.getBatteryLevel()

    def getPlantFinish(self):
        return self.__aPlantFinsih

    def PlantFinish(self):
        return self.__aPlantFinsih
