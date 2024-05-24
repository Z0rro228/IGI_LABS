from ISerializer import ISerializer
from CityModel import CountryModel


class Country:
    '''Model of country list.'''

    def __init__(self, serializer: ISerializer, filename: str):
        self.__serializer = serializer
        self.__filename = filename

    def AddCountries(self, countries: list):
        allCountr = self.__serializer.DeserializeFromFile(self.__filename)
        allCountr.extend(countries)
        self.__serializer.SerializeToFile(allCountr, self.__filename)

    def FindCountriesByCities(self, citystrlist: list):
        allCountr = self.__serializer.DeserializeFromFile(self.__filename)
        matchedCountries = []
        for cityy in citystrlist:
            for countryy in allCountr:
                city: str = countryy.city
                if (city == cityy):
                    matchedCountries.append(countryy.country)
                    matchedCountries.append(cityy)
        return matchedCountries

    def FindPopulationByCity(self, city: str):
        allCountr = self.__serializer.DeserializeFromFile(self.__filename)
        matchedCountries = []
        for countryy in allCountr:
            cityy: str = countryy.city
            if (city == cityy):
                matchedCountries.append(countryy.population)
                matchedCountries.append(cityy)
        return matchedCountries

