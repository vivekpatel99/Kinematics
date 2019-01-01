import numpy as np
import math
import matplotlib.pyplot as plt
from robot_arm_3dof import *


# Instantiate robot arm class.
Arm = RobotArm3D()

# Add desired number of joints/links to robot arm object.
Arm.add_revolute_link(length=33, thetaInit=math.radians(0))
Arm.add_revolute_link(length=105, thetaInit=math.radians(0))
Arm.add_revolute_link(length=98, thetaInit=math.radians(0))
Arm.update_joint_coords()

# print(Arm.joints)
# Initialize target coordinates to current end effector position.
target = Arm.joints[:,[-1]]
# print(target)



# Determine maximum reach of arm.
reach = sum(Arm.lengths)




def move_to_target():
    '''Run Jacobian inverse routine to move end effector toward target.'''
    global Arm, target, reach

    # Set distance to move end effector toward target per algorithm iteration.
    distPerUpdate = 0.02 * reach

    if np.linalg.norm(target - Arm.joints[:,[-1]]) > 0.02 * reach:

        targetVector = (target - Arm.joints[:,[-1]])[:3]
        targetUnitVector = targetVector / np.linalg.norm(targetVector)
        deltaR = distPerUpdate * targetUnitVector
        J = Arm.get_jacobian()
        JInv = np.linalg.pinv(J)
        deltaTheta = JInv.dot(deltaR)
        # print(deltaTheta)
        Arm.update_theta(deltaTheta)
        Arm.update_joint_coords()


targetX = 2.0
targetY =2.0
targetZ =2.0

target = np.array([[targetX, targetY, targetZ, 1]]).T
while True:
    move_to_target()
