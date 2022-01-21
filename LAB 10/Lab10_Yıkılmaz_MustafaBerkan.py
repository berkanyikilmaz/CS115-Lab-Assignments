# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:31:52 2021

@author: M. Berkan Yıkılmaz
"""

import matplotlib.pyplot as plt
import numpy as np

plt.clf()

initial = np.arange(30,75,5)
bounce = np.array([22,26,29,34,38,40,45,50,52])

plt.plot(initial, bounce, "bo")
plt.title("Initial Height vs. Bounce Height")
plt.xlabel("Initial Height")
plt.ylabel("Bounce Height")

a, b = np.polyfit(initial, bounce, 1)
predict = initial * a + b
plt.plot(initial, predict, "r")


