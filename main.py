# Created by viv at 15.12.18
"""

"""
# TODO : 1. calibrate servo \
#          2. check  pwm_generate
import time
import sys

from lib import gpio
from lib import pwm
import constants as cont
from lib import servo_calib_data as servo_calib
from lib import miscellaneous as misc
from lib import IK_3dof as ik


# ------------------------------------------------------------------------------
# """ FUNCTION: MAIN """
# ------------------------------------------------------------------------------
def main():
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



if __name__ == '__main__':
    # servo_calibration()
    main()
