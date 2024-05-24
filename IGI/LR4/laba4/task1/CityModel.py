class CountryModel:
    '''Data model of country.'''
    def __init__(self, country:str, city:str, population:str):
        self.country = country
        self.city = city
        self.population = population

    def __str__(self) -> str:
        return self.country + ' ' + self.city + ' ' + self.population