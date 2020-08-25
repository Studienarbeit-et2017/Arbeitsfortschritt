from miflora.miflora_poller import MiFloraPoller
from btlewrap.bluepy import BluepyBackend
from miflora import miflora_scanner

class PlantSensor(object):

    __aHumidity = 0.0
    __aTemperature = 0.0
    __aLight = 0.0

    def __init__(self, pMAC):
        self.__poller = MiFloraPoller(pMAC, BluepyBackend)

    def getHumidity(self):
        self.__aHumidity = self.__poller.parameter_value('moisture')
        return self.__aHumidity

    def getTemperature(self):
        self.__aTemperature = self.__poller.parameter_value('temperature')
        return self.__aTemperature

    def getLight(self):
        self.__aLight = self.__poller.parameter_value('light')
        return self.__aLight

    def getBatteryLevel(self):
        return self.__poller.parameter_value('battery')
