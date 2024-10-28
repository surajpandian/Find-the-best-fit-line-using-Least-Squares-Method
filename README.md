# Implementation of Univariate Linear Regression
### Date: 22-08-24
## AIM:
To implement univariate Linear Regression to fit a straight line using least squares.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Jupyter notebook

## Algorithm

Step 1: Start the program.

Step 2: Get the independent variable X and dependent variable Y.

Step 3: Calculate the mean of the X -values and the mean of the Y -values.4

Step 4: Find the slope m of the line of best fit using the formula. 
<img width="231" alt="121" src="https://github.com/user-attachments/assets/638a5b9f-fd3c-4668-ab97-aff21925568f">


Step 5: Compute the y -intercept of the line by using the formula:
<img width="148" alt="122" src="https://github.com/user-attachments/assets/0fa81415-7aaa-4fdd-8795-46f0f0f3b90c">


Step 6: Use the slope m and the y -intercept to form the equation of the line.

Step 7: Obtain the straight line equation Y=mX+b and plot the scatterplot.

Step 8: Stop the program.


## Program:

Program to implement univariate Linear Regression to fit a straight line using least squares.

Developed by: R suraj pandian

RegisterNumber: 212223080040

```
import numpy as np
import matplotlib.pyplot as plt

# Preprocessing Input data
X=np.array(eval(input()))
Y=np.array(eval(input()))

# Mean
X_mean=np.mean(X)
Y_mean=np.mean(Y)
num=0
denom=0

# to find sum of(xi-x') & (yi-y') & (xi-x')^2
for i in range(len(X)):
    num+=(X[i]-X_mean)(Y[i]-Y_mean)
    denom+=(X[i]-X_mean)**2

# calculate slope
m=num/denom

# calculate intercept
b=Y_mean-m*X_mean
print(m,b)

# Line equation
y_predicted=m*X+b
print(y_predicted)

# to plot graph
plt.scatter(X,Y)
plt.plot(X,y_predicted,color='red')
plt.show()
```

## Output:

14,24,53,76

23,61,43,25

-0.15976517454659817 44.67019603732047

[42.43348359 40.83583185 36.20264179 32.52804277]

![123](https://github.com/user-attachments/assets/17d869c4-a3bb-4ba0-adba-5b19f27d4d63)



## Result:
Thus the univariate Linear Regression was implemented to fit a straight line using least squares using python programming.
