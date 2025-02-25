from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time
import numpy
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    
    def __init__(self):
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
            
            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
            #                             jointName = "Torso_BackLeg", 
            #                             controlMode = p.POSITION_CONTROL, 
            #                             targetPosition = BackLegControl[i], 
            #                             maxForce = c.motorForce)
            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
            #                             jointName = "Torso_FrontLeg", 
            #                             controlMode = p.POSITION_CONTROL, 
            #                             targetPosition = FrontLegControl[i], 
            #                             maxForce = c.motorForce)
            time.sleep(c.sleepTime)

    def __del__(self):
        p.disconnect()