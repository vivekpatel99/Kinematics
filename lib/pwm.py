# Created by viv at 14.12.18

"""
servo control
 for 50Hz signal
  - 5% of duty cycle corresponds to 1ms pulse width (0 angle)
  - 10% of duty cycle corresponds to 2ms pulse width (180 angle)

"""
import gpio


class PWM:
    def __init__(self, pin_path, pin_num,  duty_cycle, frequency):
        self.pin_path = pin_path
        self.pin_num = pin_num
        self.duty_cycle = duty_cycle
        self.frequency = frequency

        # initialize gpio pin
        gpio_path = gpio.GPIO(pin_path, pin_num)
        gpio_path.export()
        gpio_path.set_direction("out")

    def pwm_calculate(self):
        # ton = duty cycle * total time or frequency
        ton = self.duty_cycle
        toff = self.frequency - ton

        return ton, toff

    def servo_set_0(self, pin_path):
        pass

    def set_duty_cycle(self):
        pass