# Created by viv at 14.12.18

"""
servo control
 for 50Hz signal
  - 5% of duty cycle corresponds to 1ms pulse width (0 angle)
  - 10% of duty cycle corresponds to 2ms pulse width (180 angle)


  - light orange - pulse
  - dark  orange - +V
  - brown        - gnd


  period T = 1 / frequency
  duty cycle D = (pulse width/T)*100
  pulse width = (duty cycle/100)*T

"""
import math
import time

import gpio

# -----------------------------------------------
""" constants """
STATE_WRITE = "1"
STATE_READ = "0"

# -----------------------------------------------
servo_min = 150 # min pulse range
servo_max = 600 # max pulse range


# ------------------------------------------------------------------------------
# """ CLASS: for PWM set up """
# ------------------------------------------------------------------------------
class PWM:
    def __init__(self, pin_path, pin_num, freq_hz = 50):
        self.pin_path = pin_path
        self.pin_num = pin_num
        self.freq_hz = float(freq_hz)

        # initialize gpio pin
        self.gpio_path = gpio.GPIO(pin_path, pin_num)
        self.gpio_path.export()
        self.gpio_path.set_direction()

    # ------------------------------------------------------------------------------
    # """ FUNCTION: to set frquency """
    # ------------------------------------------------------------------------------
    def set_pwm_freq(self, freq_hz):
        """Set the PWM frequency to the provided value in hertz."""
        prescaleval = 25000000.0  # 25MHz
        prescaleval /= 4096.0  # 12-bit
        prescaleval /= float(freq_hz)
        prescaleval -= 1.0
        print('[INFO] Setting PWM frequency to {0} Hz'.format(freq_hz))
        print('[INFO] Estimated pre-scale: {0}'.format(prescaleval))
        prescale = int(math.floor(prescaleval + 0.5))
        print('[INFO] Final pre-scale: {0}'.format(prescale))

    # ------------------------------------------------------------------------------
    # """ FUNCTION: to generate pwm pulse """
    # ------------------------------------------------------------------------------
    def set_duty_cycle(self, on_off):
        self.gpio_path.set_gpio_value(on_off)

    # ------------------------------------------------------------------------------
    # """ FUNCTION: to calculate pulse from given frequency """
    # ------------------------------------------------------------------------------
    def pwm_generate(self, duty_cycle):
        """
        ton = total time (ts) * duty cycle
        toff = ts - ton
        :return:
        """
        total_time = float(1/self.freq_hz)
        ton = float(total_time*(duty_cycle/100))
        toff = total_time - ton

        # PWM.set_duty_cycle(1)
        self.gpio_path.set_gpio_value(1)
        time.sleep(ton)

        # PWM.set_duty_cycle(0)
        self.gpio_path.set_gpio_value(0)
        time.sleep(toff)

        # return ton, toff

    # ------------------------------------------------------------------------------
    # """ FUNCTION: angle to duty cycle conversion """
    # ------------------------------------------------------------------------------
    def angle_to_dcycle(self, servo_num):
        pass


