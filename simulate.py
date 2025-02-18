import pybullet as p
import time 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

ITERATIONS = 2000

backAmplitude = numpy.pi/5
backFrequency = 0
backPhaseOffset = 0

frontAmplitude = numpy.pi/4
frontFrequency = 10 * numpy.pi
frontPhaseOffset = numpy.pi / 2

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(ITERATIONS)
frontLegSensorValues = numpy.zeros(ITERATIONS)

targetAngles = numpy.sin(numpy.linspace(0, 2 * numpy.pi, ITERATIONS)) * numpy.pi/4
#numpy.save('data/sin.npy', targetAngles)

BackLegControl = backAmplitude * numpy.sin(backFrequency * targetAngles + backPhaseOffset)
FrontLegControl = frontAmplitude * numpy.sin(frontFrequency * targetAngles + frontPhaseOffset)

for i in range(ITERATIONS):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_BackLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition = BackLegControl[i], 
                                maxForce = 20)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
                                jointName = "Torso_FrontLeg", 
                                controlMode = p.POSITION_CONTROL, 
                                targetPosition = FrontLegControl[i], 
                                maxForce = 20)
    time.sleep(1/60)

numpy.save('data/sensor.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()


