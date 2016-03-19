"""
głównym zadaniem tego modułu będzie:
- ładowanie danych zewnętrznych
- udostępnianie informacji o ilości obiektów, atrybutów,
- udostępnianie możliwości doboru typu danych do faktycznego rodzaju danych atrybutu
- podawanie zakresu danych dla atrybutu
- mapowanie wartości tekstowych na numeryczne
- podanie informacji o klasach decyzyjnych
"""

import numpy as np


class DataSet:
    rawData = np.array
    dataSetMeta = np.array
    objectCount = int
    attributeCount = int

    def __init__(self, file, separator):
        # dataSet nie powinien zostać utworzony jako pusty, więc przy tworzeniu obiektu powinny być załadowane dane
        # wydaje się, że powinny być co najmniej dwa sposoby, jeden poprzez wczytanie z pliku a drugi z tablicy
        # np. jako część dataSet-u
        self.load_data_from_file(file, separator)
        pass

    def load_data_from_file(self, file, separator):
        self.rawData = np.genfromtxt(file, delimiter=separator)
        pass

    def get_part_of_data(self, start, end):
        pass
