# Created by viv at 14.12.18
import os
import time

import miscellaneous as misc




class GPIO:
    def __init__(self, gpio_path, pin_num):

        self.export_path = "/sys/class/gpio/export"
        self.pin_num = pin_num

        if os.path.exists(gpio_path):
            self.gpio_path = gpio_path
        else:
            print("[ERROR] path does not exit {}".format(gpio_path))

    def export(self):

        if os.path.exists(self.export_path):
            misc.file_write(self.export_path, "w", self.pin_num)
        else:
            print("[ERROR] path does not exist {}".format(self.export_path))

    def set_direction(self, direction):

        dir_path = os.path.join(self.gpio_path, "direction")
        misc.file_write(dir_path, "w", direction)

    def set_gpio_value(self, value):

        dir_path = os.path.join(self.gpio_path, "value")
        misc.file_write(dir_path, "w", value)

def main():

    gpio_913 = "/sys/class/gpio/gpio913"

    gpio_913 = GPIO(gpio_913, "913")
    gpio_913.set_direction("out")
    gpio_913.set_gpio_value("1")
    time.sleep(10)

if __name__ == "__main__":
    main()