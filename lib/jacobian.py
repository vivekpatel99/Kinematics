# Created by viv at 01.01.19

import numpy as np
import math
import constants as const

class Link:
    def __init__(self, theta=0, alpha=0, r=0,  D=0):
        self.alpha = float(math.radians(alpha))
        self.r = float(r)
        self.theta = float(math.radians(theta))
        self.D = float(D)

    # def __str__(self):
    #     return "Link(theta={}, alpha={}, r={}, D={})".format(self.alpha,self.r, self.theta, self.D)


class RoboticArm:
    def __init__(self, name = "robot"):
        self.alpha = []
        self.r = []
        self.thetas = []
        self.d = []

        self.name = name

        self.xroot = 0
        self.yroot = 0
        self.zroot = 0

        self.link_count = 0

    def add_revolute_link(self, **kwargs):
        # self.joints = np.append(self.joints, np.array([[0, 0, 0, 1]]).T, axis=1)
        # self.lengths.append(kwargs['length'])
        # self.thetas = np.append(self.thetas, kwargs.get('thetaInit', 0))
        # self.DH += [kwargs]
        self.thetas = np.append(self.thetas, math.radians(kwargs.get('theta', 0)))
        self.alpha = np.append(self.alpha, math.radians(kwargs.get('alpha', 0)))
        self.r = np.append(self.r, kwargs.get('r', 0))
        self.d = np.append(self.d, kwargs.get('d', 0))
        self.link_count += 1

    def __str__(self):
        "Robot Name: ".format(self.name)

        for i in range(len(self.thetas)):
            print("Link(theta={}, alpha={}, r={}, D={})".format(self.thetas[i], self.alpha[i], self.r[i], self.d[i]))

        return " "

    def get_homog_trans_matrix(self, idx):
        """
        thetas[idx]
        alpha[idx]
        r[idx]
        d[idx]
        """

        """
         homogeneous Transformation matrix
               _                                                                                                     _
              |                                                                                                       |
              | cos(theta_n),    -sin(theta_n) * cos(alpha_n),     sin(theta_n) * sin(alpha_n),    r_n * cos(theta_n) |
              | sin(theta_n),     cos(theta_n) * cos(alpha_n),    -cos(theta_n) * sin(alpha_n),    r_n * sin(theta_n) |
        H_n = |       0     ,            sin(alpha_n)        ,             cos(alpha_n)       ,           d_n         |
              |       0     ,                  0             ,                  0             ,            1          |
              |_                                                                                                     _|
        """
        print(self.thetas[idx], self.alpha[idx], self.r[idx], self.d[idx])

        homog_trans_matrix = [
                        [np.cos(self.thetas[idx]), -np.sin(self.thetas[idx]) * np.cos(self.alpha[idx]), np.sin(self.thetas[idx]) * np.sin(self.alpha[idx]), self.r[idx] * np.cos(self.thetas[idx])],
                        [np.sin(self.thetas[idx]), np.cos(self.thetas[idx]) * np.cos(self.alpha[idx]), -np.cos(self.thetas[idx]) * np.sin(self.alpha[idx]), self.r[idx] * np.sin(self.thetas[idx])],
                        [0, np.sin(self.alpha[idx]), np.cos(self.alpha[idx]), self.d[idx]],
                        [0, 0, 0, 1],
                    ]
        return homog_trans_matrix

    def update_joint_coords(self):
        Hn = []

        # taking the number of rows from the DH parameters
        for i in range(self.link_count):
            print(i)
            H = self.get_homog_trans_matrix(i)

            if i == 0:
                Hn = H

            else:
                Hn = np.dot(Hn, H)


        return Hn

if __name__=="__main__":
    Robo = RoboticArm()
    Robo.add_revolute_link(theta=const.THETA_1, alpha=90, r=0, d=const.L_1)
    Robo.add_revolute_link(theta=const.THETA_2, alpha=0, r=0, d=const.L_2)
    Robo.add_revolute_link(theta=const.THETA_2, alpha=0, r=0, d=const.L_3)
    Hn = Robo.update_joint_coords()
    print(np.matrix(Hn))
