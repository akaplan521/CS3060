import constants as c
import numpy 
import pybullet as p
import pyrosim.pyrosim as pyrosim


class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act() 

    def Prepare_To_Act(self):
        self.amplitude = c.backAmplitude  
        
        # using joint index to make the even numbered joints move at twice speed as odd ones
        self.jointIndex = pyrosim.jointNamesToIndices[self.jointName]
        if self.jointIndex % 2 == 0:  
            self.frequency = c.backFrequency
        else:  
            self.frequency = c.backFrequency * 0.5 

        self.offset = c.backPhaseOffset 

        self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi, c.ITERATIONS) + self.offset)

    def Set_Value(self, robot, t): 
        
        targetPosition = self.motorValues[t]  

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotId,  
            jointName=self.jointName,  
            controlMode=p.POSITION_CONTROL,  
            targetPosition=targetPosition,  
            maxForce=c.motorForce  
        )

    def Save_Values(self):
        numpy.save(f"data/{self.jointName}_motor.npy", self.motorValues)
        print(f"Motor values for {self.jointName} saved to data/{self.jointName}_motor.npy")