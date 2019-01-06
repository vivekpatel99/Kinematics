# Created by viv at 06.01.19
import sys

import numpy as np
import math
import constants as const

import time

from lib import fk


def get_jacobian(fkine_obj):

    Hn = fkine_obj.fk()

    R0_0 = [
            [0.],
            [0.],
            [1.]
    ]

    D0_n = Hn[:, 3][:-1]

    # print(D0_n)

    upper_part = np.cross(R0_0, D0_n, axis=0)
    # print("upper_part")
    # print(upper_part)
    for i in range(1, np.shape(const.PT_2dof)[0]):
        H0_i = fkine_obj.homog_trans_matrix(i)

        # accessing 3rd column of the matrix and removing last row
        R0_i = H0_i[:, 2][:-1]

        # accessing 4th column of the matrix and removing last row
        D0_i = H0_i[:, 3][:-1]

        col = np.cross(R0_i, np.subtract(D0_n, D0_i), axis=0)

        upper_part = np.concatenate([upper_part, col], axis=1)

    return upper_part[:-1]


# ------------------------------------------------------------------------------
# """ FUNCTION: MAIN """
# ------------------------------------------------------------------------------
def jacob_test():
    angle_1 = 0.
    angle_2 = 90.

    x_dot = 1.
    y_dot = 1.

    a4 = 105
    a2 = 33.

    while 180. >= angle_1 >= 0. and 180. >= angle_2 >= 0.:

        angle_1 = math.radians(angle_1)
        angle_2 = math.radians(angle_2)

        sa1 = np.sin(angle_1)
        sa2 = np.sin(angle_2)

        ca2 = np.cos(angle_2)
        ca1 = np.cos(angle_1)

        j11 =  (a4 * sa1 * ca2) - (a4 * ca1 * sa2) - (a2 * sa1)
        j12 = -(a4 * sa1 * ca2) - (a4 * ca1 * sa2)
        j21 =  (a4 * ca1 * ca2) - (a4 * sa1 * sa2) + (a2 * ca1)
        j22 =  (a4 * ca1 * ca2) - (a4 * sa1 * sa2)

        jacobian = [[j11, j12],
                    [j21, j22]]


        mult = 1.0 / ((j11 * j22) - (j12 * j21))

        j11_inv = mult * j22
        j21_inv = mult * (-j21)
        j12_inv = mult * (-j12)
        j22_inv = mult * j11

        theta_1_dot = (j11_inv * x_dot) + (j12_inv * y_dot)
        inc_theta_1 = theta_1_dot / 100.

        theta_2_dot = (j21_inv * x_dot) + (j22_inv * y_dot)
        inc_theta_2 = theta_2_dot / 100.

        angle_1 = angle_1 + inc_theta_1
        angle_2 = angle_2 + inc_theta_2

        angle_1 = math.degrees(angle_1)
        angle_2 = math.degrees(angle_2)

    print("test theta_1 {} test theta_2 {}".format(angle_1, angle_2))


# ------------------------------------------------------------------------------
# """ FUNCTION: MAIN """
# ------------------------------------------------------------------------------
def main():
    f_kine = fk.Fkine(const.PT_2dof)

    x_dot = 1.
    y_dot = 1.

    while math.radians(180.) >= const.PT_2dof[0][0] >= math.radians(0.) and math.radians(180.) >= const.PT_2dof[1][
        0] >= math.radians(0.):

        jacobian = get_jacobian(f_kine)
        print(jacobian)
        jacobian_inv = np.linalg.inv(jacobian)

        # print(jacobian_inv)
        theta_1_dot, theta_2_dot = jacobian_inv.dot([x_dot, y_dot])
        print(jacobian_inv.dot([x_dot, y_dot]))


        inc_theta_1 = theta_1_dot / 100.
        inc_theta_2 = theta_2_dot / 100.

        const.PT_2dof[0][0] = inc_theta_1
        const.PT_2dof[1][0] = inc_theta_2

    print("theta_1 {} theta_2 {}".format(const.PT_2dof[0][0], const.PT_2dof[1][0]))


if __name__ == '__main__':
    main()
