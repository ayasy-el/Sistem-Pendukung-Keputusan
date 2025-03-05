import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(3.0, 3.0, 200)
y = numpy.random.normal(3.0, 2.0, 200)

plt.scatter(x,y)
plt.savefig("scatter.png")