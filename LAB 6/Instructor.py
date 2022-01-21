# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:43:34 2021

@author: M. Berkan Yıkılmaz
"""

class Instructor():
    def __init__(self, inst_id, name, status, hours):
        self.__id = inst_id
        self.__name = name
        self.__status = status
        self.__hours = hours
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_status(self):
        return self.__status
    
    def get_hours(self):
        return self.__hours
    
    def calculate_salary(self):
        if self.__status.lower() == 'f':
            return 5000 + self.__hours * 500
        elif self.__status.lower() == 'p':
            return self.__hours * 400
            
    def __str__(self):
        return f'Name:{self.__name}\nStatus: {self.__status}\nSalary: {self.calculate_salary():.1f} TL\n'
        
    def __repr__(self):
        return f'Id:{self.__id}\nName:{self.__name}\nSalary: {self.calculate_salary():.1f} TL\n'
    

    
    
    
    
    