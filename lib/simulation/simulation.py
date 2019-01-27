# Created by viv at 10.01.19

import numpy as np
import matplotlib.pyplot as plt

# Input the desired position and rotation of the platform
p = np.array([[0.0], [0.0]])
R = np.array([[1.0, 0.], [0., 1.]])

# Design variables
l1 = np.array([[0.], [0.]])
l2 = np.array([[0.], [0.]])

b1 = np.array([[0.], [0.]])
b2 = np.array([[0.], [0.]])


#Calculate the outputs

s1 = p+ np.dot(R, b1) - l1
s2 = p+ np.dot(R, b2) - l2

len_s1 = np.sqrt(s1[0]**2 + s1[1]**2)
len_s2 = np.sqrt(s2[0]**2 + s2[1]**2)

plt.plot([l1[0], s1[0] + l1[0], p[0], s2[0]+l2[0], l2[0], l1[1], s1[1] + l1[1], p[1], s2[1]+l2[1], l2[1]])
