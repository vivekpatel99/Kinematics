# Created by viv at 15.12.18
"""

"""
import math
import time
import sys
import numpy as np
from lib import pwm
import constants as cont
from lib import servo_calib_data as servo_calib
from lib import miscellaneous as misc
from lib import ik_3dof as ik
from lib import fk

from lib.jacobian import jacobian

# ------------------------------------------------------------------------------
# """ FUNCTION: MAIN """
# ------------------------------------------------------------------------------
def main_old():
    """
    906
    :return:
    """

    pwm_jf7 = pwm.PWM(cont.JF7_MIO0_906, "906")
    pwm_jf8 = pwm.PWM(cont.JF8_MIO09_915, "915")
    pwm_jf9 = pwm.PWM(cont.JF9_MIO14_920, "920")

    while True:
        X = float(input("X: "))
        Y = float(input("Y: "))
        Z = float(input("Z: "))
        theta_1, theta_2, theta_3 = ik.ik_3dof(X, Y, Z)
        # theta_1 = 1.0
        # theta_2 = 50.0
        # theta_3 = 50.0
        pwm_jf7.pwm_generate(misc.angle_to_dcycle(servo_calib.servo_1, theta_1))
        time.sleep(0.5)

        pwm_jf8.pwm_generate(misc.angle_to_dcycle(servo_calib.servo_2, theta_2))
        time.sleep(0.5)

        pwm_jf9.pwm_generate(misc.angle_to_dcycle(servo_calib.servo_3, theta_3))
        time.sleep(0.5)
        sys.exit(-1)

# ------------------------------------------------------------------------------
# """ FUNCTION: MAIN """
# ------------------------------------------------------------------------------
def main():
    """
    step #1 : find R3_6 = inv R0_3 * R0_6
    step #2 : find R3_6 by denavit hartenberg or other methods

    step #3 : R0_6 depends on the requirement
             suppose gripper will be on facing on Z direction thus, the R0_6 matrix will be comparison with R0_1

                  _       _
                 | 0  0  1 |
         R0_6 =  | 0 -1  0 |
                 | 1  0  0 |
                  -       -

    :return:
    """
    theta_1, theta_2, theta_3 = ik.ik_3dof(2.0, 2.0, 2.0)
    print(theta_1)
    print(theta_2)
    print(theta_3)
    # R0_3 = fk.fkine_3dof()
    # # print(np.matrix(R0_3))
    # R0_3 = [
    #             R0_3[0][:3],
    #             R0_3[1][:3],
    #             R0_3[2][:3]
    #         ]
    # # print(np.matrix(R0_3))
    # # R0_5 = [
    # #             [0.0, 0.0, -1.0],
    # #             [0.0, -1.0, 0.0],
    # #             [1.0, 0.0, 0.0]
    # #         ]
    # R0_5 = [
    #             [-1.0, 0.0, 0.0],
    #             [0.0, -1.0, 0.0],
    #             [0.0, 0.0, 1.0]
    #         ]
    # invR0_3 = np.linalg.inv(R0_3)
    #
    # R3_5 = np.dot(invR0_3, R0_5)
    # # print(np.matrix(R3_5))
    #
    # theta_5 = np.arccos(R3_5[2][1])
    # # theta_4 = np.arcsin(R3_5[1][0]/-np.sin(theta_5))
    # theta_4 = np.arcsin(R3_5[1][2])
    # print(theta_4)
    #
    # R3_6_check = [
    #                 [-np.sin(theta_4) * np.cos(theta_5), np.sin(theta_4) * np.sin(theta_5),     np.cos(theta_4)],
    #                 [ np.cos(theta_4) * np.cos(theta_5), np.cos(theta_4) * (-np.sin(theta_5)),  np.sin(theta_4)],
    #                 [          np.sin(theta_5),                  np.cos(theta_5),                 0       ]
    #               ]
    # # print()
    # # print(np.matrix(R3_6_check))
    # print(misc.rad_to_deg(theta_4))
    # print(misc.rad_to_deg(theta_5))

    # fk.test_fkine(theta_1, theta_2, theta_3, theta_4, theta_5)
if __name__ == '__main__':
    # servo_calibration()
    # main()

    jacobian.main()

    print()
    print('jacobian caculation test')

    jacobian.jacob_test()

    fk = fk.Fkine(cont.PT_2dof)
    print(fk.fk())