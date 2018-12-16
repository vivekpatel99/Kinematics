# Created by viv at 14.12.18
import os
import time

import miscellaneous as misc


# -----------------------------------------------
""" constants """
DIRECTION = "direction" # create path to direction dir for set gpio direction
WRITE = "w" # use to set gpio out










# ------------------------------------------------------------------------------
# """ CLASS: for GPIO set up """
# ------------------------------------------------------------------------------
class GPIO:
    def __init__(self, gpio_path, pin_num):

        self.export_path = "/sys/class/gpio/export"
        self.unexport_path = "/sys/class/gpio/unexport"
        self.pin_num = pin_num

        if os.path.exists(gpio_path):
            self.gpio_path = gpio_path
        else:
            print("[ERROR] path does not exit {}".format(gpio_path))

        # need to unexport otherwise it will through error "resources are busy"
        if os.path.exists(self.unexport_path):
            misc.file_into_write(self.unexport_path, WRITE, self.pin_num)
            print("[INFO] unexport successful {}".format(self.pin_num))
        else:
            print("[ERROR] path does not exist {}".format(self.unexport_path))

    # ------------------------------------------------------------------------------
    # """ FUNCTION: to export gpio"""
    # ------------------------------------------------------------------------------
    def export(self):

        if os.path.exists(self.export_path):
            misc.file_into_write(self.export_path, WRITE, self.pin_num)
            print("[INFO] export successful {}".format(self.pin_num))
        else:
            print("[ERROR] path does not exist {}".format(self.export_path))

    # ------------------------------------------------------------------------------
    # """ FUNCTION: to set direction of gpio input or output"""
    # ------------------------------------------------------------------------------
    def set_direction(self, direction="out"):

        dir_path = os.path.join(self.gpio_path, DIRECTION)

        misc.file_into_write(dir_path, WRITE, direction)
        print("[INFO] direction set {} {}".format(direction, self.pin_num))

    # ------------------------------------------------------------------------------
    # """ FUNCTION: to set gpio 1 or 0"""
    # ------------------------------------------------------------------------------
    def set_gpio_value(self, value):

        dir_path = os.path.join(self.gpio_path, "value")
        misc.file_into_write(dir_path, WRITE, value)

# ----------------------------------------------------------------------------------------------------------------------
# """ FUNCTION: main """
# ----------------------------------------------------------------------------------------------------------------------
def main():

    gpio_913 = "/sys/class/gpio/gpio913"

    gpio_913 = GPIO(gpio_913, "913")
    gpio_913.set_direction("out")
    gpio_913.set_gpio_value("1")
    time.sleep(10)

if __name__ == "__main__":
    main()