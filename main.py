# Created by viv at 15.12.18
"""

"""
import math
import time
import sys
import numpy as np
import robopy as rpy

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
def robo_main():
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
    step #2 : find R3_6 by Denavit Hartenberg or other methods

    step #3 : R0_6 depends on the requirement
             suppose gripper will be on facing on Z direction thus, the R0_6 matrix will be comparison with R0_1

                  _       _
                 | 0  0  1 |
         R0_6 =  | 0 -1  0 |
                 | 1  0  0 |
                  -       -

    :return:
    """

    theta_1, theta_2, theta_3 = ik.ik_3dof(126, 106, 216.)
    print(math.degrees(theta_1), math.degrees(theta_2), math.degrees(theta_3))
    fk_3dof = fk.Fkine(cont.PT_3dof)
    # removing last row and last column to get only rotation matrix
    R0_3 = fk_3dof.fk()[:, :-1][:-1]
    # print(R0_3)
    R0_5 = [
                [-1., 0., 0.],
                [0., -1., 0.],
                [0., 0., 1.]
            ]
    # R0_5 = [
    #             [0., 0., 1.],
    #             [0., -1., 0.],
    #             [1., 0., 0.]
    #         ]
    invR0_3 = np.linalg.inv(R0_3)

    R3_5 = invR0_3.dot(R0_5)
    print(R3_5)
    theta_5 = np.arccos(R3_5[2, 1])

    # theta_4 = np.arcsin(R3_5[1][0]/-np.sin(theta_5))

    theta_4 = np.arcsin(R3_5[1, 2])  # [row][column]
    print(math.degrees(theta_4), math.degrees(theta_5))

    R3_6_check = np.matrix([
                    [-np.sin(theta_4) * np.cos(theta_5), np.sin(theta_4) * np.sin(theta_5),     np.cos(theta_4)],
                    [ np.cos(theta_4) * np.cos(theta_5), np.cos(theta_4) * (-np.sin(theta_5)),  np.sin(theta_4)],
                    [          np.sin(theta_5),                  np.cos(theta_5),                 0       ]
                  ])
    print()
    print(np.matrix(R3_6_check))

    # print(math.degrees(theta_4))
    # print(math.degrees(theta_5))

    print("##### output ####")

    L_1 = 33.  # mm 3.3cm
    L_2 = 105.  # mm 10.5cm
    L_3 = 98.  # mm 9.8cm
    L_4 = 27.  # mm 2.7cm
    L_5 = 65.  # mm 6.5cm

    PT_5dof = [
        [theta_1, math.radians(90.0), 0, L_1],
        [theta_2, 0, L_2, 0],
        [theta_3, 0, L_3, 0],
        [theta_4 + math.radians(90.0), math.radians(90.0), 0, 0],
        [theta_5, 0, 0, L_4 + L_5]
    ]
    # fk.test_fkine(theta_1, theta_2, theta_3, theta_4, theta_5)
    fk_5dof = fk.Fkine(PT_5dof)
    # removing last row and last column to get only rotation matrix
    print(fk_5dof.fk())
if __name__ == '__main__':
    tstart = time.time()
    # servo_calibration()
    main()
    # fk = fk.Fkine(cont.PT_5dof)
    # print(fk.homog_trans_matrix(0))
    # print()
    # jacobian.main()

    # jacobian.jacob_test()
    #
    # rob = rpy.Joyit()
    #
    # # l = np.array([0, 0, 0,0,0])
    # # xyz = rob.fkine(stance = l, unit='deg')
    # # print(xyz)
    #
    # PX = 1.
    # PY = 1.
    # PZ = 1.
    #
    # T = np.mat([[1, 0, 0, PX],
    #             [0, 1, 0, PY],
    #             [0, 0, 1, PZ],
    #             [0, 0, 0, 1],
    #             ])
    #
    # angle = rob.ikine(T, q0=[0, 0, 0, 0, 0], unit='deg')
    #
    # print(angle)
    # print("Total time {}".format(time.time() - tstart))
