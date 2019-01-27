# Created by viv at 22.12.18

from collections import namedtuple
import sys

#                                (x1, y1)    (x2, y2)
# Servo = namedtuple("Servo", ['angle_0', 'angle_180'])
Servo = namedtuple("Servo", ['start_pnt', 'end_pnt'])
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
#    limits of robotic arm     actual limits
servo_1 = Servo((0., 0.),
                (180., 9.5)) # 9.5

servo_2 = Servo((0., 1.),     # 0.0.
                 (180., 5.))  # 4 (5dof safety limit)  # 9.2 (3dof safety limit) # 9.5 (limit)

servo_3 = Servo((0., 0.),
                (180., 6.)    # 4 (5dof safety limit ) # 7. (3dof safety limit)  # 9.4 (limit)
                )

servo_4 = Servo((0., 0.),
                (180., 6.))  # 4 (5dof safety limit ) # 9. (3dof safety limit)  # 10  (limit)


servo_5 = Servo((0., 0.),
                (180., 8.))  # 10


# testing entered servo calibration data
servos_tuple = (servo_1, servo_2, servo_3, servo_4, servo_5)

for servo in servos_tuple:

    if servo[0][0] != 0.:
        print("[ERROR] please set proper servo limits".format(servo))
        sys.exit(1)

    elif servo[1][0] != 180.:
        print("[ERROR] please set proper servo limits".format(servo))
        sys.exit(1)

    elif type(servo[0][1]) != float or type(servo[1][1]) != float:
        print("[WARNING] servo calibration values should be in float".format(servo))

    elif not servo[0][1] < 15. or not servo[1][1] < 15.:
        print("[ERROR] servo limits must be less than 15% duty cycle".format(servo))
        sys.exit(1)
    elif not servo[0][1] < servo[1][1]:
        print("[ERROR] servo minimum limit must be less than maximum limit".format(servo))
        sys.exit(1)
    else:
        pass
