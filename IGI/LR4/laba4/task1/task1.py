from ISerializer import ISerializer
from CityModel import CountryModel
from CSVSerializer import CSVSerializer
from PickleSerializer import PickleSerializer
from Country import Country


def task1():
    try:
        print("Task 1.")
        serializer: ISerializer
        filename: str
        lst = [CountryModel("Belarus", "Minsk","474"), CountryModel("GreatBritain", "Manchester","9876"),]
        lst2 = ["London","Minsk","Paris"]

        print("Введите способ сериализации (1 - csv, 2 - pickle)")
        chs = input()
        if (chs == '1'):
            serializer = CSVSerializer
            filename = 'task1.csv'
        elif (chs == '2'):
            serializer = PickleSerializer
            filename = 'task1.pickle'
        else:
            raise ValueError

        clist = Country(serializer, filename)
        ''' clist.AddCountries(lst)'''
        print("Countries and cities")
        print(clist.FindCountriesByCities(lst2))
        print('Enter city you want to search:')
        sch = input()
        print(clist.FindPopulationByCity(sch))

    except ValueError as e:
        print("Value error!!! Try again...")

task1()
