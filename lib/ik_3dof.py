# Created by viv at 08.12.18

import math
import numpy as np


def make_val_in_range(val, min_range=-1, max_range=1):
    if val < min_range:
        return -1

    elif val > max_range:
        return 1
    else:
        return val


def ik_3dof(X=0, Y=0, Z=0):
    # Desired X Y position of the end effector in cm

    # length of each joint
    joint_len_1 = 33.  # mm 3.3cm
    joint_len_2 = 105.  # mm 10.5cm
    joint_len_3 = 98.  # mm 9.8cm

    # theta_1 = np.arctan(Y, X) # eq1
    theta_1 = math.atan(Y / X)  # eq1
    r1 = np.sqrt(X ** 2 + Y ** 2)  # eq2
    r2 = Z - joint_len_1  # eq3
    phi_2 = math.atan(r2 / r1)  # eq4
    r3 = np.sqrt(r1 ** 2 + r2 ** 2)  # eq5

    phi_1_eq = (((joint_len_3 ** 2) - (joint_len_2 ** 2) - (r3 ** 2)) / (-2.0 * joint_len_2 * r3))

    phi_1 = np.arccos(make_val_in_range(phi_1_eq, min_range=-1, max_range=1))  # eq6

    theta_2 = phi_2 - phi_1  # eq7

    phi_3_eq = (((r3 ** 2) - (joint_len_2 ** 2) - (joint_len_3 ** 2)) / (-2.0 * joint_len_2 * joint_len_3))
    phi_3 = np.arccos(make_val_in_range(phi_3_eq, min_range=-1, max_range=1))  # eq8
    theta_3 = np.pi - phi_3  # eq9

    return theta_1, theta_2, theta_3


if __name__ == "__main__":
    ik_3dof(50.0, 60.0, 60.0)
