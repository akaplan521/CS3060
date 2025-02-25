# import pybullet as p
# import time 
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import constants as c


# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(c.ITERATIONS)
# frontLegSensorValues = numpy.zeros(c.ITERATIONS)

# targetAngles = numpy.sin(numpy.linspace(0, 2 * numpy.pi, c.ITERATIONS)) * numpy.pi/4
# #numpy.save('data/sin.npy', targetAngles)

# BackLegControl = c.backAmplitude * numpy.sin(c.backFrequency * targetAngles + c.backPhaseOffset)
# FrontLegControl = c.frontAmplitude * numpy.sin(c.frontFrequency * targetAngles + c.frontPhaseOffset)



# numpy.save('data/sensor.npy', backLegSensorValues)
# numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
# p.disconnect()

from simulation import SIMULATION

simulation = SIMULATION()
simulation.run()
