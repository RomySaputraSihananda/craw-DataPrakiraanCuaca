import requests
from requests import Response
import xmltodict 
import xml.etree.ElementTree as ET
from json import dumps
from datetime import datetime

class Bmkg:
    def __init__(self) -> None:
        self.__BASE_URL: str = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/'
        self.__result: dict = {}
        self.__result['timestamp']: str = None
        self.__result['source']: str = None
        self.__result['productioncenter']: str = None
        self.__result['data']: list = []

    def __str_2_datetime(self, text: str) -> str:
        return datetime.strptime(text, "%Y%m%d%H%M%S").strftime("%Y-%m-%dT%H:%M:%S");

    def __filter_area(self, areas: list):
        for area in areas:
            self.__result['data'].append({
                "kabupaten" : {name['@xml:lang'] : name['#text'] for name in area['name']},
                "provinsi" : area['@domain']
            })


    def execute(self, provinsi: str) -> str:
        url = self.__BASE_URL + f"DigitalForecast-{provinsi}.xml"
        res: Response = requests.get(url)

        data = xmltodict.parse(res.content.decode('utf-8'))

        self.__result['timestamp']: str = self.__str_2_datetime(data['data']['forecast']['issue']['timestamp'])
        self.__result['source']: str = data['data']['@source']
        self.__result['productioncenter']: str = data['data']['@productioncenter']

        self.__filter_area(data['data']['forecast']['area'])
        
        print(self.__result)


# testing
if(__name__ == "__main__"):
    bmkg: Bmkg = Bmkg()

    bmkg.execute('Aceh')