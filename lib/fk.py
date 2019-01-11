# Created by viv at 08.12.18

import numpy as np
import miscellaneous as misc

# PT = [[0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       ]






def main():

    theta_1 = 0.0
    theta_2 = 0.0
    theta_3 = 90.0

    a1 = 33. # mm 3.3cm
    a2 = 105. # mm 10.5cm
    a3 = 98. # mm 9.8cm

    # PT = [[misc.deg_to_rad(90.0), misc.deg_to_rad(90.0), 0, a1+d1],
    #       [misc.deg_to_rad(90.0), misc.deg_to_rad(-90.0), 0, a2+d2],
    #       [0, 0, 0, a3+d3],
    #       ]
    PT = [[misc.deg_to_rad(theta_1), misc.deg_to_rad(90.0), 0, a1],
          [misc.deg_to_rad(theta_2), 0, a2, 0],
          [misc.deg_to_rad(theta_3), 0, a3, 0],
          ]

    """
     homogeneous matrix
           _                                                                                                     _
          |                                                                                                       |
          | cos(theta_n),    -sin(theta_n) * cos(alpha_n),     sin(theta_n) * sin(alpha_n),    r_n * cos(theta_n) |
          | sin(theta_n),     cos(theta_n) * cos(alpha_n),    -cos(theta_n) * sin(alpha_n),    r_n * sin(theta_n) |
    H_n = |       0     ,            sin(alpha_n)        ,             cos(alpha_n)       ,           d_n         |
          |       0     ,                  0             ,                  0             ,            1          |
          |_                                                                                                     _|
    """
    Hn = []

    for i in range(3):
        H = [
                [np.cos(PT[i][0]), -np.sin(PT[i][0]) * np.cos(PT[i][1]), np.sin(PT[i][0]) * np.sin(PT[i][1]), PT[i][2] * np.cos(PT[i][0])],
                [np.sin(PT[i][0]), np.cos(PT[i][0]) * np.cos(PT[i][1]), -np.cos(PT[i][0]) * np.sin(PT[i][1]), PT[i][2] * np.sin(PT[i][0])],
                [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
                [0, 0, 0, 1],
            ]
        Hn.append(H)

    H0_2 = np.dot(Hn[0], Hn[1])
    H0_3 = np.dot(H0_2, Hn[2])

    # print(np.matrix(H0_3))
    print(np.matrix(H0_3[0][3]))
    print(np.matrix(H0_3[1][3]))
    print(np.matrix(H0_3[2][3]))






if __name__ == "__main__":
    main()