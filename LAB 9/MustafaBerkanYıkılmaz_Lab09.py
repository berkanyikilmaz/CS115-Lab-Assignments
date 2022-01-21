# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:34:08 2021

@author: M. Berkan Yıkılmaz
"""
import numpy as np

covid_data = np.loadtxt('covid_data.txt')
covid_country = np.loadtxt("covid_country.txt", dtype = 'str', skiprows = 1)

covid_data = covid_data.T

tests = np.max(covid_data[:,2])
print("Maximum test per 1 million:", tests)

asia_countries = covid_country[covid_country[:,1] == "Asia"]
print("Countries in Asia:", asia_countries[:,0])

ind = np.where(covid_data[:,1] < 50)
print("Countries with less than 50 deaths per 1 million:", covid_country[ind[:],0])

eu_ind = np.where(covid_country[:,1] == 'Europe')
avg_case = np.mean(covid_data[eu_ind,0])
print("Average cases per 1 million in Europe:", avg_case)

countries = covid_country[eu_ind,0]
case = covid_data[eu_ind,0]
#min_case = np.argmin(case)
min_case = np.min(case)
all_min_ind = np.where(case[0,:] == min_case)
#print("Country with minimum total cases per 1 million in Europe:", countries[0, min_case])
print("Country with minimum total cases per 1 million in Europe:", countries[0, all_min_ind])

test_result = np.array([covid_country[:,0],covid_data[:,1]]).T

np.savetxt("test_data.txt", test_result, fmt = '%s')




