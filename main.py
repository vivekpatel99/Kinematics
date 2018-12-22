# Created by viv at 15.12.18
"""

"""
# TODO : 1. calibrate servo \
#          2. check  pwm_generate
import time

from lib import gpio
from lib import pwm
import constants as cont
from lib import servo_calib_data as servo_calib


# ------------------------------------------------------------------------------
# """ FUNCTION: to set servo pulse """
# ------------------------------------------------------------------------------
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length /= 50
    print('{0}us per period'.format(pulse_length))
    pulse_length /= 4096
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    print(pulse_length)
    pulse /= pulse_length
    print(pulse)
    pulse = round(pulse)
    print(pulse)
    pulse = int(pulse)
    print(pulse)
    # pwm.set_pwm(channel, 0, pulse)


# ------------------------------------------------------------------------------
# """ FUNCTION: angle to duty cycle conversion """
# ------------------------------------------------------------------------------
def angle_to_dcycle(servo_num, angle):
    """
    calculation
    (0,0)
    (180,10)
    - fit the line of these two points, to get duty cycle for an angle
    - the slop of two point is
     m = (y2-y1)/(x2-x1)
     y-y1 = m(x-x1)
     where y = duty cycle
           x = angle
    """
    if angle >= 180:
        angle = 180

    if angle <= 0:
        angle = 0

    slop = (servo_num.end_pnt[1] - servo_num.start_pnt[1]) / (servo_num.end_pnt[0] - servo_num.start_pnt[0])

    duty_cycle = (slop * (angle - servo_num.start_pnt[0])) + servo_num.start_pnt[1]

    return duty_cycle


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
    # pwm_jf2 = pwm.PWM(cont.JF2_MIO10_916, "916")
    # pwm_jf3 = pwm.PWM(cont.JF3_MIO11_917, "917")
    # duty = input("duty: ")
    # duty = 5

    while (True):
        angle = float(input("angle 0 - 180 : "))
        pwm_jf7.pwm_generate(angle_to_dcycle(servo_calib.servo_1, angle))
        time.sleep(0.5)

        pwm_jf8.pwm_generate(angle_to_dcycle(servo_calib.servo_2, angle))
        time.sleep(0.5)

        pwm_jf9.pwm_generate(angle_to_dcycle(servo_calib.servo_3, angle))




if __name__ == '__main__':
    # servo_calibration()
    main()
