# Created by viv at 06.01.19

"""
#1 while angle is in between 0 and 180
#2 calculate Jacobian
#3 calculate inverse of Jacobian
#4 calculate theta_dots by multiplying xyz dots to inverse Jacobian
#5 calculate increment
#6 use the increment to set an angle of servo after converting it into degrees

"""
import numpy as np
import math
import sys
import time

import constants as const
from lib import fk


def get_jacobian(fkine_obj, PT):
    Hn = fkine_obj.fk()
    # print(Hn)
    R0_0 = [
        [0.],
        [0.],
        [1.]
    ]
    D0_n = Hn[:, 3][:-1]

    upper_part = np.cross(R0_0, D0_n, axis=0)
    # print(upper_part)

    # reading the number of columns from the PT, because the columns will be the same always in DH parameters
    for i in range(np.shape(PT)[0] - 1):
        H0_i = fkine_obj.homog_trans_matrix(i)

        # accessing 3rd column of the matrix and removing last row
        R0_i = H0_i[:, 2][:-1]

        # accessing 4th column of the matrix and removing last row
        D0_i = H0_i[:, 3][:-1]

        next_col = np.cross(R0_i, np.subtract(D0_n, D0_i), axis=0)

        upper_part = np.concatenate([upper_part, next_col], axis=1)

    return upper_part


# ------------------------------------------------------------------------------
# """ FUNCTION: MAIN """
# ------------------------------------------------------------------------------
def _jacob_test():
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

        j11 = (a4 * sa1 * ca2) - (a4 * ca1 * sa2) - (a2 * sa1)
        j12 = -(a4 * sa1 * ca2) - (a4 * ca1 * sa2)
        j21 = (a4 * ca1 * ca2) - (a4 * sa1 * sa2) + (a2 * ca1)
        j22 = (a4 * ca1 * ca2) - (a4 * sa1 * sa2)

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
def jacob_test():
    theta_1 = math.radians(0)
    theta_2 = math.radians(90)

    x_dot = 1.
    z_dot = 1.

    L_1 = 33.
    L_2 = 105
    cnt = 0
    while 180. >= math.degrees(theta_1) >= 0. and 180. >= math.degrees(theta_2) >= 0.:
        sth_1 = np.sin(theta_1)
        sth_2 = np.sin(theta_2)

        cth_1 = np.cos(theta_1)
        cth_2 = np.cos(theta_2)

        j11 = - L_1 * sth_1 * cth_2
        j12 = - L_2 * cth_1 * sth_2

        j21 = 1.
        j22 = 2 * L_2 * cth_2

        jacobian = [[j11, j12],
                    [j21, j22]]

        mult = 1.0 / ((j11 * j22) - (j12 * j21))

        j11_inv = mult * j22
        j21_inv = mult * (-j21)
        j12_inv = mult * (-j12)
        j22_inv = mult * j11

        theta_1_dot = (j11_inv * x_dot) + (j12_inv * z_dot)
        inc_theta_1 = theta_1_dot / 100.

        theta_2_dot = (j21_inv * x_dot) + (j22_inv * z_dot)
        inc_theta_2 = theta_2_dot / 100.

        theta_1 += inc_theta_1
        theta_2 += inc_theta_2
        cnt += 1
        print(cnt)
    print("test theta_1 {} test theta_2 {}".format(math.degrees(theta_1), math.degrees(theta_2)))


# ------------------------------------------------------------------------------
# """ FUNCTION: MAIN """
# ------------------------------------------------------------------------------
def main():

        # 1 while angle is in between 0 and 180
        # 2 calculate Jacobian
        # 3 calculate inverse of Jacobian
        # 4 calculate theta_dots by multiplying xyz dots to inverse Jacobian
        # 5 calculate increment
        # 6 use the increment to set an angle of servo after converting it into degrees

    THETA_1 = 0.1
    THETA_2 = 90.
    THETA_3 = 0.1
    THETA_4 = 0.1
    THETA_5 = 0.1

    L_1 = 33.  # mm 3.3cm
    L_2 = 105.  # mm 10.5cm
    L_3 = 98.  # mm 9.8cm
    L_4 = 27.  # mm 2.7cm
    L_5 = 65.  # mm 6.5cm

    PT = [
        [math.radians(THETA_1), math.radians(90.0), 0, L_1],
        [math.radians(THETA_2), 0, L_2, 0],
        [math.radians(THETA_3), 0, L_3, 0],
        [math.radians(THETA_4) + math.radians(90.0), math.radians(90.0), 0, 0],
        [math.radians(THETA_5), 0, 0, L_4 + L_5]
    ]

    x_dst = 1.
    y_dst = 1.
    z_dst = 1.
    i = 0
    while 180. >= math.degrees(PT[0][0]) >= 0. \
            and 180. >= math.degrees(PT[1][0]) >= 0. \
            and 180. >= math.degrees(PT[2][0]) >= 0. \
            and 180. >= math.degrees(PT[3][0]) >= 0. \
            and 180. >= math.degrees(PT[4][0]) >= 0.:

        fk_5d = fk.Fkine(PT)
        jacobian = get_jacobian(fk_5d, PT)

        jacobian_inv = np.linalg.pinv(jacobian)
        # print(jacobian_inv)
        # print()
        for row in range(np.shape(jacobian_inv)[1]):
            for column in range(np.shape(jacobian_inv)[0]):
                if jacobian_inv[column][row] < 0.00009:
                    jacobian_inv[column][row] = 1.
                # print(jacobian_inv[column][row])
                # print()

        current_cord = fk_5d.fk()[:, 3][:-1]

        theta_dots = jacobian_inv.dot([
            [x_dst],
            [y_dst],
            [z_dst],
        ])
        # print(theta_dots)
        PT[0][0] += theta_dots.item(0) / 100
        PT[1][0] += theta_dots.item(1) / 100
        PT[2][0] += theta_dots.item(2) / 100
        PT[3][0] += theta_dots.item(3) / 100
        PT[4][0] += theta_dots.item(4) / 100

        i += 1
        print(i)

    print("theta_1 {}".format(math.degrees(PT[0][0])))
    print("theta_2 {}".format(math.degrees(PT[1][0])))
    print("theta_3 {}".format(math.degrees(PT[2][0])))
    print("theta_4 {}".format(math.degrees(PT[3][0])))
    print("theta_5 {}".format(math.degrees(PT[4][0])))


if __name__ == '__main__':
    main()
