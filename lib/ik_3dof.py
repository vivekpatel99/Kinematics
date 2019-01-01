# Created by viv at 08.12.18



import math
import numpy as np
import miscellaneous as misc
import  constants as const

def ik_3dof(X, Y, Z):
    # Desired X Y position of the end effector in cm
    X = float(X)
    Y = float(Y)
    Z = float(Z)


    # theta_1 = np.arctan(Y, X) # eq1
    theta_1 = math.atan(Y / X)  # eq1
    r1 = np.sqrt(X ** 2 + Y ** 2)  # eq2
    r2 = Z - const.L_1  # eq3
    phi_2 = math.atan(r2 / r1)  # eq4
    r3 = np.sqrt(r1 ** 2 + r2 ** 2)  # eq5

    phi_1 = np.arccos((const.L_3 ** 2 - const.L_2 ** 2 - r3 ** 2) / (-2.0 * const.L_2 * r3))  # eq6

    theta_2 = phi_2 - phi_1  # eq7

    phi_3 = np.arccos(((r3 ** 2) - (const.L_2 ** 2) - (const.L_3 ** 2)) / (-2.0 * const.L_2 * const.L_3)) # eq8
    theta_3 = np.pi - phi_3  # eq9

    return theta_1, theta_2, theta_3
    # print(misc.rad_to_deg(theta_1), misc.rad_to_deg(theta_2), misc.rad_to_deg(theta_3))
    # return misc.rad_to_deg(theta_1), misc.rad_to_deg(theta_2), misc.rad_to_deg(theta_3)


if __name__ == "__main__":
    ik_3dof(50.0,60.0, 60.0)