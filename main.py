# Created by viv at 15.12.18
"""

"""
import math
import time
import sys
import numpy as np

# -----------------------------------------------
from lib import pwm
import constants as const
from lib import servo_calib_data as servo_calib
from lib import miscellaneous as misc
from lib.kinematics import ikine as ik


# ------------------------------------------------------------------------------
# """ FUNCTION: To control Servos with IK algorithm """
# ------------------------------------------------------------------------------
def robo_main():
    """
    906
    :return:
    """

    pwm_jf7 = pwm.PWM(const.JF7_MIO0_906, "906")
    pwm_jf8 = pwm.PWM(const.JF8_MIO09_915, "915")
    pwm_jf9 = pwm.PWM(const.JF9_MIO14_920, "920")

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

    """
    end_eff_direction_mat = np.matrix([
        [-1., 0., 0.],
        [0., -1., 0.],
        [0., 0., 1.]
    ])

    thetas = ik.ik_5dof(end_eff_direction_mat, 5, 5, 5)

    print("theta_1 {}".format(math.degrees(thetas.theta_1)))
    print("theta_2 {}".format(math.degrees(thetas.theta_2)))
    print("theta_3 {}".format(math.degrees(thetas.theta_3)))
    print("theta_4 {}".format(math.degrees(thetas.theta_4)))
    print("theta_5 {}".format(math.degrees(thetas.theta_5)))


if __name__ == '__main__':
    tstart = time.time()

    main()

    print("Total time {}".format(time.time() - tstart))
