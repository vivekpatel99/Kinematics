# Created by viv at 16.12.18
# Created by viv at 10.12.18
import os

import numpy as np



# ------------------------------------------------------------------------------
# """ FUNCTION: to convert degree to radian """
# ------------------------------------------------------------------------------
def deg_to_rad(deg):
    return deg*(np.pi/180)
    # return (deg/180)*np.pi
# ------------------------------------------------------------------------------
# """ FUNCTION: to convert radian to degree """
# ------------------------------------------------------------------------------
def rad_to_deg(rad):
    return rad*(180/np.pi)

# ------------------------------------------------------------------------------
# """ FUNCTION: to open file and write something """
# ------------------------------------------------------------------------------
def write_into_file(path, mode, value):

    if not os.path.exists(path):
        print("[ERROR] path does not exist {}".format(path))
    try:
        with open(path, mode) as fil:

            fil.write(str(value))
            # return True

    except Exception as error:
        print(error, path)
        # raise

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
