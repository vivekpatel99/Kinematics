# Created by viv at 10.12.18

import numpy as np

def deg_to_rad(deg):
    return deg*(np.pi/180)
    # return (deg/180)*np.pi

def rad_to_deg(rad):
    return rad*(180/np.pi)


def file_into_write(path, mode, value):

    try:
        with open(path, mode) as fil:
            fil.write(value)
            return True

    except Exception as error:
        print(error, path)
        raise