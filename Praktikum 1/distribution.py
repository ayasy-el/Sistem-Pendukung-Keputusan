import numpy
import matplotlib.pyplot as plt

x= numpy.random.uniform(0.0,5.0,250)
# x= numpy.random.uniform(0.0,5.0,(250,5))
# x = numpy.mean(x,axis=1)

# print(x)

plt.hist(x,20)
plt.savefig("histogram.png")