import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/sensor.npy')

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()