import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.ITERATIONS)

    def Get_Value(self, t):  
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == c.ITERATIONS - 1:
            print(f"{self.linkName} Sensor Values:", self.values)

    def Save_Values(self):
        numpy.save(f"data/{self.linkName}_sensor.npy", self.values)
        print(f"Sensor values for {self.linkName} saved to data/{self.linkName}_sensor.npy")