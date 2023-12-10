from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD
from pymycobot.genre import Coord
import time
import os
import sys
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
import time

mc = MyCobot("COM5", 115200)
mc.send_angles([0, 0, 0, 0, 0, 0], 50)
time.sleep(0.5)
mc.send_angles([0, 90, -60, 40, 0, 0], 50)
time.sleep(0.5)

i=2
while i > 0:
    print("::get_coords() ==> coordinates: {}\n".format(mc.get_coords()))
    time.sleep(5)

mc.release_all_servos()