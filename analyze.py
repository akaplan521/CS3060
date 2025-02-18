import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/sensor.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
sinVals = numpy.load('data/sin.npy')

#matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 4)
#matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")
matplotlib.pyplot.plot(sinVals, numpy.sin(sinVals))
matplotlib.pyplot.xlabel('Angle [rad]')
matplotlib.pyplot.ylabel('sin(x)')
matplotlib.pyplot.axis('tight')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()