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
from io import StringIO


class DataSet:
    rawData = []
    dataSetNames = []
    objectCount = int
    attributeCount = int

    def __init__(self, file, separator):
        # dataSet nie powinien zostać utworzony jako pusty, więc przy tworzeniu obiektu powinny być załadowane dane
        # wydaje się, że powinny być co najmniej dwa sposoby, jeden poprzez wczytanie z pliku a drugi z tablicy
        # np. jako część dataSet-u
        self.load_data_from_file(file, separator)

    def load_data_from_file(self, file, separator):
        # otwarcie pliku i odczytanie pierwszej linii
        with open(file, 'r') as f:
            first_line = f.readline()
        self.dataSetNames = np.loadtxt(StringIO(first_line), dtype=bytes, delimiter=separator).astype(str)
        self.rawData = np.genfromtxt(file, delimiter=separator, skip_header=1)
        self.objectCount = self.rawData.shape[0]
        self.attributeCount = self.rawData.shape[1] - 1

    def get_part_of_data(self, start, end):
        return self.rawData[start:end, :]

    def get_total_number_of_classes(self):
        return np.unique(self.rawData[:, self.rawData.shape[1] - 1:self.rawData.shape[1]]).size

    def get_number_of_elements_in_classes(self):
        unique, counts = np.unique(self.rawData[:, self.rawData.shape[1] - 1:self.rawData.shape[1]], return_counts=True)
        print(np.asarray((unique, counts)).T)
