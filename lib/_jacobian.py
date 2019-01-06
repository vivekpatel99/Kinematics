# Created by viv at 01.01.19

import numpy as np
import math
import constants as const
import time

class Link:
    def __init__(self, theta=0, alpha=0, r=0,  d=0):
        self.theta = float(math.radians(theta))
        self.alpha = float(math.radians(alpha))
        self.r = float(r)
        self.d = float(d)


    def __str__(self):
        return "Link(theta={}, alpha={}, r={}, d={})".format(self.theta, self.alpha, self.r, self.d)

    def __dir__(self):
        return [self.theta, self.alpha, self.r, self.d]

    @property
    def change_theta(self):
        return self.theta

    @change_theta.setter
    def change_theta(self, value):
        self.theta = value

class Fkine:

    def __init__(self, links=None, PT=None):
        if PT is None:
            self.PT = []
            for j in links:
                self.PT.append([j.theta, j.alpha, j.r, j.d])
        else:
            self.PT = PT

    @property
    def change_thetas(self):
        return self.PT

    @change_thetas.setter
    def change_thetas(self, *args):

        for idx, ar in enumerate(args[0]):
            self.PT[idx][0] = ar






    def homog_trans_matrix(self, row_num):
        """
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

        homog_trans_matrix = [
                        [np.cos(self.PT[row_num][0]), -np.sin(self.PT[row_num][0]) * np.cos(self.PT[row_num][1]), np.sin(self.PT[row_num][0]) * np.sin(self.PT[row_num][1]), self.PT[row_num][2] * np.cos(self.PT[row_num][0])],
                        [np.sin(self.PT[row_num][0]), np.cos(self.PT[row_num][0]) * np.cos(self.PT[row_num][1]), -np.cos(self.PT[row_num][0]) * np.sin(self.PT[row_num][1]), self.PT[row_num][2] * np.sin(self.PT[row_num][0])],
                        [0, np.sin(self.PT[row_num][1]), np.cos(self.PT[row_num][1]), self.PT[row_num][3]],
                        [0, 0, 0, 1],
                    ]
        return homog_trans_matrix

    # ------------------------------------------------------------------------------
    # """ FUNCTION: to Calculate forward kinematics """
    # ------------------------------------------------------------------------------


    def fkine(self, frame_num = None):
        """ function to generate forward kinematic from DH parameters
            by multiplying homogeneous transformation matrix Hn = H_0 * H_1 * ....H_n-1
        """
        Hn = []

        if frame_num is not None:
            # to find endeffector of any frame
            rotaion_mat = range(frame_num)
        else:
            rotaion_mat = range(np.shape(self.PT)[0])

        # taking the number of rows from the DH parameters
        for i in rotaion_mat:
            H = self.homog_trans_matrix(i)

            if i == 0:
                Hn = H

            else:
                Hn = np.dot(Hn, H)

        return np.mat(Hn)

class RoboticArm(Fkine):
    def __init__(self, links=None, name = "robot"):

        Fkine.__init__(self, links)
        self.name = name

        self.xroot = 0
        self.yroot = 0
        self.zroot = 0

    def get_jacobian(self):
        """"""
        """
        only for revolute joints
        _  _      _
       | °x |    |
       | °y |    |
       | °z | =  |
       | wx |    |
       | wy |    |
       |_wz_|    |_
        
        """
        """
        https://www.youtube.com/watch?v=SefTCXrpL8U&t=24s
        """

        """
               [[0],
        R0_i-1  [0], X (d0_n - d0_i-1)
                [1]]
                
               [[0],
        R0_i-1  [0], 
                [1]] 
                 
            
         [[°x][°y][°z][wz][wy][]wz]  =          R0_0[[0][0][1]] X (d0_2 -d0_0)   R0_1[[0],[0],[1]] X (d0_2-d0_1) .[[theta_1][theta_2]}
                                                R0_0[[0][0][1]]                  R0_1[[0],[0],[1]]               
       
      
       """
        # TODO #1: take H0_n from fk
        # TODO #2: for loop until length of the theta list to  find H0_1 and save it into column of the  upper matrix and  save it into another matrix called lower mat
        # TODO #3:  get displacement vector from H0_1 and minus it from H0_n
        # TODO #4  do cross product of the current column with displacement vector and save it into the column
        # TODO #5 continue the loop
        # R0_0 is alway identity matrix , there is not any rotation frame R0 to it self

        H0_n = self.fkine()

        # R0_0 = np.transpose([0., 0., 1.])
        R0_0 = np.array([[0.], [0.], [1.]])
        # D0_n =np.transpose((H0_n[:, 3])[:-1])
        D0_n =H0_n[:, 3][:-1]

        upper_part = np.array(np.cross(R0_0, D0_n, axis=0))

        lower_part = R0_0

        for i in range(1, np.shape(self.PT)[0]):
            H0_i = self.fkine(frame_num=i)

            # accessing 3rd column of the matrix and removing last row
            R0_i = H0_i[:, 2][:-1]

            # accessing 4th column of the matrix and removing last row
            D0_i = H0_i[:, 3][:-1]

            col = np.array(np.cross(R0_i, np.subtract(D0_n, D0_i), axis=0))

            upper_part = np.concatenate([upper_part, col], axis=1)

            # lower_part = np.concatenate([lower_part, R0_i], axis=1)

        # Jacobian = np.concatenate([upper_part,lower_part], axis=0)



        # jacobian = upper_part * theta_list

        # print(np.matrix(jacobian_inv))

        return upper_part

if __name__=="__main__":

    tim = time.time()
    theta_1 = 10
    theta_2 = 10
    theta_3 = 10

    L_1 = Link(theta=theta_1, alpha=90, r= 0, d = 33)
    L_2 = Link(theta=theta_2, alpha=0, r= 105, d = 0)
    L_3 = Link(theta=theta_3, alpha=0, r= 98, d = 0)

    Robo = RoboticArm([L_1, L_2, L_3], name="JOY-IT")

    x_dst = 20.
    y_dst = 20.
    z_dst = 20.

    # accessing 3rd column of the matrix and removing last row
    x_current, y_current, z_current = Robo.fkine()[:,3][:-1]
    print("x_current {}, y_current {}, z_current {}".format(x_current, y_current, z_current))

    x_chng = x_current - x_dst
    y_chng = y_current - y_dst
    z_chng = z_current - z_dst

    i = 0
    while (x_chng > 0.05 or x_chng < -0.05) or (y_chng > 0.05 or y_chng < -0.05) or (z_chng > 0.05 or z_chng < -0.05):
        i +=1

        jacobian = Robo.get_jacobian()

        jacobian_inv = np.linalg.inv(jacobian)

        inc_mat = np.mat([
                            [x_dst],
                            [y_dst],
                            [z_dst]
                        ])

        theta_change = jacobian_inv.dot(inc_mat)

        theta_1 = theta_1 + theta_change.item(0)
        theta_2 = theta_2 + theta_change.item(1)
        theta_3 = theta_3 + theta_change.item(2)

        Robo.change_thetas = theta_change.item(0), theta_change.item(1), theta_change.item(2)

        x_new, y_new, z_new = Robo.fkine()[:, 3][:-1]

        # print( x_new, y_new, z_new)
        # break

        x_chng = x_new - x_dst
        y_chng = y_new - y_dst
        z_chng = z_new - z_dst
        print("x_new {}, y_new {}, z_new {}".format(x_new, y_new, z_new))

        # print("Xchange {}, Ychange {}, Zchange {}".format(x_chng, y_chng, z_chng))
        # if i== 100:
        #     break

    print(theta_1, theta_2, theta_3)

    print("total time {}".format(time.time() - tim))

