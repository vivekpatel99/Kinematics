# Created by viv at 23.12.18

import sys

import pwm

sys.path.append("../")
import constants as cont

# ------------------------------------------------------------------------------
# """ FUNCTION: servo calibration """
# ------------------------------------------------------------------------------
def servo_calibration():
    """
    906
    :return:
    """
    pwm_jf7 = pwm.PWM(cont.JF7_MIO0_906, "906")
    pwm_jf8 = pwm.PWM(cont.JF8_MIO09_915, "915")
    pwm_jf9 = pwm.PWM(cont.JF9_MIO14_920, "920")
    # pwm_jf2 = pwm.PWM(cont.JF2_MIO10_916, "916")
    # pwm_jf3 = pwm.PWM(cont.JF3_MIO11_917, "917")
    # duty = input("duty: ")
    # duty = 5

    while (True):
        # angle = int(input("angle: "))
        angle = float(input("PWM pulse duty cycle  0-10: "))

        # pwm_jf7.pwm_generate(angle)
        # time.sleep(0.5)

        # pwm_jf8.pwm_generate(angle)
        # time.sleep(0.5)

        pwm_jf9.pwm_generate(angle)




if __name__ == "__main__":
    servo_calibration()