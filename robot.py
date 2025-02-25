from sensor import SENSOR
from motor import MOTOR
import pybullet as p

class ROBOT:
    def __init__(self, s=0, m=0):
        self.robotId = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
