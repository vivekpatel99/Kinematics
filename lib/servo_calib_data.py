# Created by viv at 22.12.18

from collections import namedtuple
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

servo_1 = Servo((0.0, 0.0),
                (180.0, 10.0)
                )

servo_2 = Servo((0.0, 0.0),
                (180.0, 9.5)
                )

servo_3 = Servo((0.0, 0.0),
                (180.0, 9.4)
                )

servo_4 = Servo(1.0, 9.0)
servo_5 = Servo(1.0, 9.0)
servo_6 = Servo(1.0, 9.0)
