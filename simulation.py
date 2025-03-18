from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time
import numpy
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robotId)

        self.backLegSensorValues = numpy.zeros(c.ITERATIONS)
        self.frontLegSensorValues = numpy.zeros(c.ITERATIONS)

        self.targetAngles = numpy.sin(numpy.linspace(0, 2 * numpy.pi, c.ITERATIONS)) * numpy.pi / 4

        self.BackLegControl = c.backAmplitude * numpy.sin(c.backFrequency * self.targetAngles + c.backPhaseOffset)
        self.FrontLegControl = c.frontAmplitude * numpy.sin(c.frontFrequency * self.targetAngles + c.frontPhaseOffset)


    def run(self):
        for i in range(c.ITERATIONS):
            # print(i)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think(i)
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(0.01)
            else:
                time.sleep(c.sleepTime)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        #save sensor and motor values here if wanted
        p.disconnect()