# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:52:44 2021

@author: M. Berkan Yıkılmaz
"""

import matplotlib.pyplot as plt
import numpy as np

student = np.loadtxt("students.txt", skiprows = 1)
half_scholarship = np.where(student[:,0] == 2)
half = student[half_scholarship,:][0]

plt.figure(1)
plt.clf()

full_scholarship = np.where(student[:,0] == 1)
full = student[full_scholarship,:][0]

plt.subplot(2,2,1)
res = plt.hist(half[:,3],4)
plt.title("Frequency of Writing Gr. of Half Sc. Students")

plt.subplot(2,2,2)
x_axis = np.arange(1, half.size / 4 + 1, 1)
plt.plot(x_axis, half[:,1], "*")
plt.plot(x_axis, half[:,2], "-")
plt.title("Math vs Reading Gr. of Half Sc. Students")
plt.ylabel("Grades")
plt.legend(["Math", "Reading"])

plt.subplot(2,2,3)
labels = ["Full","Half","Non"]
a = round((full.size / student.size) * 100, 1)
b = round((half.size / student.size) * 100, 1)
c = 100 - (a + b)
sizes = [a, b, c]
explode = [0, 0, 0.1]
plt.pie(sizes, explode = explode, labels = labels, autopct='%1.1f%%')
plt.title("Scholarship Percentages")

plt.subplot(2,2,4)
half_avg = np.sum(half[:,2]) / (half.size / 4)
all_avg = np.sum(student[:,2]) / (student.size / 4)
plt.bar("Half-sc", half_avg)
plt.bar("All", all_avg)
plt.title("Reading Grades: Half Sc. vs All Students")
plt.ylabel("Average of Grades")
plt.plot()

plt.show()