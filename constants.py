import numpy

ITERATIONS = 800

backAmplitude = numpy.pi/5
backFrequency = 20
backPhaseOffset = 0

frontAmplitude = numpy.pi/4
frontFrequency = 10 * numpy.pi
frontPhaseOffset = numpy.pi / 2

motorForce = 20
gravity = -9.8

sleepTime = 1/60

numberOfGenerations = 1
populationSize = 1

numSensorNeurons = 3
numMotorNeurons = 2