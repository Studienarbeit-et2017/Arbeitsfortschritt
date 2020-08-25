import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

#influxdb Data
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
token = "a8gXheTesNsdpiwdRaamhrtZpyKPdnW8mDfKvHkpBpOG8itNjHr5thRYs6AHLkd59QaGa8VGOsmP0OhkVjor7w=="
org = "studienarbeit19@gmx.de"
bucketName = "Pflanzenbewaesserung"

dbClient = InfluxDBClient(url=url, token=token, org=org)
write_api = dbClient.write_api(write_options=SYNCHRONOUS)

def updatePlantData(pPlant):
    recordData = influxdb_client.Point("measurements").tag("ID", pPlant.getID()).field("Temperatur", pPlant.getTemperature()).field("Humidity", pPlant.getHumidity()).field("Light", pPlant.getLight()).field("WaterLevel", pPlant.getWater()).field("Time", pPlant.getTime()).field("Name", pPlant.getName()).field("PlantFinish", pPlant.getPlantFinish()).field("Battery", pPlant.getBatteryLevel())
    write_api.write(bucket=bucketName, org=org, record=recordData)