import numpy

ITERATIONS = 2000

backAmplitude = numpy.pi/5
backFrequency = 20
backPhaseOffset = 0

frontAmplitude = numpy.pi/4
frontFrequency = 10 * numpy.pi
frontPhaseOffset = numpy.pi / 2

motorForce = 20
gravity = -9.8

sleepTime = 1/60

numberOfGenerations = 10
populationSize = 10

numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = 0.2

movementThreshold = 0.1 # for final project velocity variable

fitnessVariants = 0 
