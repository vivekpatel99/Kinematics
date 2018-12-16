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

