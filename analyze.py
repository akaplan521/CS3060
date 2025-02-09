import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/sensor.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 4)
matplotlib.pyplot.plot(frontLegSensorValues, label = "Front Leg")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()