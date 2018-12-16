# Created by viv at 08.12.18



import math
import numpy as np
from lib import _miscellaneous as misc

# Desired X Y position of the end effector in cm
X = 50.0
Y = 50.0
Z = 0.0
# length of each joint
joint_len_1 = 20.0
joint_len_2 = 50.0
joint_len_3 = 40.0


# theta_1 = np.arctan(Y, X) # eq1
theta_1 = math.atan(Y / X)  # eq1
r1 = np.sqrt(X ** 2 + Y ** 2)  # eq2
r2 = Z - joint_len_1  # eq3
phi_2 = math.atan(r2 / r1)  # eq4
r3 = np.sqrt(r1 ** 2 + r2 ** 2)  # eq5

phi_1 = np.arccos((joint_len_3 ** 2 - joint_len_2 ** 2 - r3 ** 2) / (-2.0 * joint_len_2 * r3))  # eq6

theta_2 = phi_2 - phi_1  # eq7

phi_3 = np.arccos(((r3 ** 2) - (joint_len_2 ** 2) - (joint_len_3 ** 2)) / (-2.0 * joint_len_2 * joint_len_3)) # eq8
theta_3 = np.pi - phi_3  # eq9

print(theta_1, theta_2, theta_3)
print(misc.rad_to_deg(theta_1), misc.rad_to_deg(theta_2), misc.rad_to_deg(theta_3))
