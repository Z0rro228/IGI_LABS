from ISerializer import  ISerializer
from CityModel import CountryModel
import csv

class CSVSerializer(ISerializer):
    '''Serializer using csv.'''
    @staticmethod
    def SerializeToFile(objs:list, filename:str):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in objs:
                writer.writerow(o.__dict__.values())

    @staticmethod
    def DeserializeFromFile(filename:str) -> list:
        try:

            with open(filename, 'r', newline='') as f:
                lst = []
                reader = csv.reader(f)
                for row in reader:
                    lst.append(CountryModel(row[0], row[1], row[2]))
            return lst
        except FileNotFoundError:
            return []