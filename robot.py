from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:

    def __init__(self, solutionID, bodyFile):
        self.robotId = p.loadURDF(bodyFile)
        
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        #os.system("del brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices: 
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t):
        for sensor in self.sensors.values():  
            sensor.Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                if t > c.ITERATIONS - 3:
                    print(f"[{t}] Acting on joint: {jointName}, angle: {desiredAngle:.4f}")
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
            
    
    def Think(self, t):
        self.nn.Update()
        self.nn.Print()
       
    def Get_Fitness(self, solutionID, movingTimesteps):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)  
        basePosition = basePositionAndOrientation[0]  
        xPosition = basePosition[0]  
        #xPosition = max(0, basePosition[0])

        movement_ratio = movingTimesteps / c.ITERATIONS
        #combined_fitness = xPosition * movement_ratio
        
        if c.fitnessVariants == 0:
            combined_fitness = xPosition
        elif c.fitnessVariants == 1:
            combined_fitness = xPosition * movement_ratio
        elif c.fitnessVariants == 2:
            combined_fitness = xPosition * (movement_ratio ** 2)
        elif c.fitnessVariants == 3:
            combined_fitness = 0.5 * xPosition - 0.5 * movement_ratio
        elif c.fitnessVariants == 4:
            k = 2  #can change this constant
            combined_fitness = xPosition + k * (1 - movement_ratio)
              
        with open("tmp" + solutionID + ".txt", "w") as file:
            file.write(f"{xPosition},{movement_ratio},{combined_fitness}")

        
        os.rename("tmp" + str(solutionID) + ".txt" , "fitness" + str(solutionID) + ".txt")
        
