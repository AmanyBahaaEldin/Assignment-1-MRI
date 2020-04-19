# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:34:34 2020

@author: ALIENWARE
"""

import matplotlib.pyplot as plt
import random

random.seed(1)
NonUniform=[]
for i in range(45):
    NonUniform.append(random.uniform(2.5 , 3.5))
    i+=1


plt.ylim(0, 6)
plt.xlim(0,40)
plt.plot(NonUniform)
plt.suptitle('Non_Uniformity')
plt.ylabel('Bz(z)')
plt.xlabel('z-axis')
plt.show()