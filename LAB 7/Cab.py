# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:31:28 2021

@author: M. Berkan Yıkılmaz
"""

class Cab():
    def __init__(self, cabType, kms, year):
        self.__typeOfCab = cabType
        self.__kms = int(kms)
        self.__year = int(year)
        
    def get_type(self):
        return self.__typeOfCab
    
    def get_kms(self):
        return self.__kms
    
    def get_year(self):
        return self.__year
    
    def __gt__(self, other):
        if self.__typeOfCab == other.__typeOfCab:
            return self.__year > other.__year
    
    def __eq__(self, other):
        if (self.__typeOfCab == other.__typeOfCab) and (self.__year == other.__year):
            return True
        return False
    
    def __repr__(self):
        return f'{self.__typeOfCab}'
    
class Sedan(Cab):
    def __init__(self, cabType, kms, year):
        Cab.__init__(self, cabType, kms, year)
        self.__pricePerKm = 2.5
        
    def calculate_fare(self):
        return self.get_kms() * self.__pricePerKm
    
class Hatchback(Cab):
    def __init__(self, cabType, kms, year):
        Cab.__init__(self, cabType, kms, year)
        self.__pricePerKm = 2.2
        
    def calculate_fare(self):
        return self.get_kms() * self.__pricePerKm
    

        