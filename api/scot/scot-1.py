from pylab import *
from scot.datatools import randomize_phase
np.random.seed(1234)
s = np.sin(np.linspace(0,8*np.pi,1000)).T
x = np.vstack([s, s, np.sign(s), np.sign(s)]).T
y = randomize_phase(x)
subplot(2,1,1)
title('Phase randomization of 2 sine waves and 2 rectangular waves')
plot(x)
subplot(2,1,2)
plot(y)
plt.show()