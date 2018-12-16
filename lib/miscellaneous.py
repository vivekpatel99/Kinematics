# Created by viv at 10.12.18

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
def file_into_write(path, mode, value):

    try:
        with open(path, mode) as fil:
            fil.write(value)
            return True

    except Exception as error:
        print(error, path)
        raise