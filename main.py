# Created by viv at 15.12.18
"""

"""

import time

from lib import gpio
from lib import pwm
import constants as cont

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
    # print(pulse)
    pulse = round(pulse)
    # print(pulse)
    pulse = int(pulse)
    print (pulse)
    # pwm.set_pwm(channel, 0, pulse)

# ------------------------------------------------------------------------------
# """ FUNCTION: to open file and write something """
# ------------------------------------------------------------------------------
def main():

    # gpio_LED = gpio.GPIO(cont.LD04_MIO07_913, "913")
    # gpio_JF1 = gpio.GPIO(cont.JF1_MIO13_191, "919")
    # gpio_LED.set_direction("out")
    # gpio_LED.set_direction("out")
    #
    #
    #
    # gpio_913.set_gpio_value("1")
    # time.sleep(10)

    pwm_led = pwm.PWM(cont.LD04_MIO07_913, "913", 5, 50)
    pwm_jf1 = pwm.PWM(cont.JF1_MIO13_919, "919", 5, 50)
    # pwm_led.set_duty_cycle()
    ton_led_pluse = pwm_led.servo_pulse_calculate()
    ton = pwm_jf1.servo_pulse_calculate()

    print(ton_led_pluse)
    print(ton)
    while(True):

        pwm_led.set_duty_cycle('1')
        pwm_jf1.set_duty_cycle('1')
        time.sleep(0.0015)

        pwm_led.set_duty_cycle('0')
        pwm_jf1.set_duty_cycle('0')
        time.sleep(0.1)


if __name__ == '__main__':
    main()
    # set_servo_pulse(0, 1.5)