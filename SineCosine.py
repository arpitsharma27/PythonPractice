import numpy as np
import math
import matplotlib.pylab as plt

x=np.linspace(-360,360,45)*np.pi/180
plt.subplot(111)
_sin=plt.plot(x, np.sin(x),label="Sine Curve")
_cos=plt.plot(x,np.cos(x),label="Cos Curve")
#_tan=plt.plot(x,np.tan(x),label="Tan Curve")
plt.legend(['sin','cos','tan'])