import numpy as np
import matplotlib.pyplot as plt
x = np.array(eval(input()))
y = np.array(eval(input()))
xmean = np.mean(x)
ymean = np.mean(y)
num=0
denom=0
for i in range(len(x)):
  num+=(x[i]-xmean)*(y[i]-ymean)
  denom+=(x[i]-xmean)**2
m=num/denom
b=ymean-m*xmean
print(m,b)
y_predicted = m*x+b
print(y_predicted)
plt.scatter(x,y)
plt.plot(x,y_predicted)
plt.show()