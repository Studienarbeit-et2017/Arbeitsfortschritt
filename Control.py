import InfluxDB
import threading
#import RaspberryPiConfig

from Mail import EMail
from Learn import Learn
from LevelControl import LevelControl
from Plant import Plant



class Control(object):

    aLearn = Learn()
    aEMail = EMail()
    aLevelControl = True #LevelControl(RaspberryPiConfig.INLevelControle)

    __Name = ""
    __alistPlant = []
    __amaxPlant = 3
    __aID = 0

    aWaterPump = False
    aValve_1 = False
    aValve_2 = False
    aValve_3 = False
    aValve_4 = False


    def __init__(self):
        for i in range(0,4):
            self.__alistPlant.append(Plant(i, "empty"))


    def new_Plant(self, pName, pTime, pWaterlevel, pValue):
        self.__alistPlant[pValue].newPlant(pValue, pName, pTime, pWaterlevel, self.aLearn.getMACSensor(pValue))

    def clear_Plant(self, pID):
        self.__alistPlant[pID].newPlant(pID, "empty", 0.0, 0.0, "")

    def getNumberOfPlants(self):
        return len(self.__alistPlant)

    def updatePlantData(self):
        for i in range(0,4):
            if (self.getName(i) != "empty"):
                InfluxDB.updatePlantData(self.__alistPlant[i])

    def Water(self):
        for i in range (0, len(self.__alistPlant)):
             if not self.__alistPlant[i].getPlantFinish():
                if 50 <= self.__alistPlant[i].aPflanzensensor.getFeuchtigkeit():
                    self.aWaterPump = True

                    if i == 0 : self.aValve_1 = True
                    elif i == 1: self.aValve_2 = True
                    elif i == 2: self.aValve_3 = True
                    elif i == 3: self.aValve_4 = True

                else:

                    if i == 0 : self.aValve_1 = False
                    elif i == 1: self.aValve_2 = False
                    elif i == 2: self.aValve_3 = False
                    elif i == 3: self.aValve_4 = False

                    if not self.aValve_1 and not self.aValve_2 and not self.aValve_3 and not self.aValve_4:
                        self.aWaterPump = False

    def PlantFinish(self, pID):
        if self.__alistPlant[pID-1].PlantFinish():
            print("Pflanze fertig")

    def PlantChangeTime(self, pTime):
        for i in range (0, len(self.__alistPlant)):
            self.__alistPlant[i].changeTime(pTime)


    #Kommunikation mit Gui
    #-----------------------------------------------------------------------------------------------------

    def getPlantID(self, pPlantnamen):
         for i in range (0, len(self.__alistPlant)):
            if self.__alistPlant[i].getName() == pPlantnamen:
                return self.__alistPlant[i].getID()

    def getName(self, Plantnumber):
        return self.__alistPlant[Plantnumber].getName()
    
    def doRefresh(self):
        #Datentraffic entlasten
        #Refreshcount = 0
        #if (Refreshcount < 10):
        #    Refreshcount = Refreshcount + 1
        #else:
        #    self.updatePlantData()
        #    Refreshcount = 0
        self.updatePlantData()
    
    def addBasics(self):
        self.new_Plant("Tomate", 5.5, 51465, 2)
        self.new_Plant("Kartoffel", 5.5, 51465, 1)
        self.new_Plant("Zucchini", 5.5, 51465, 3)

    #-----------------------------------------------------------------------------------------------------


