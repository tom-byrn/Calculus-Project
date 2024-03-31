import math
import matplotlib
import matplotlib.pyplot as plt
import numpy
import numpy as np
from matplotlib.patches import Polygon

#TAKE ALL INPUTS FROM USER
print("Enter the Objects acceleration in the form of ax^3 + bx^2 + cx + d")
coefficients=[]

for i in range (0, 4):
    while True:
        try:
            coefficient = int(input(f'Enter coefficient x^{3-i}: '))
            coefficients.append(coefficient)
            break
        except ValueError:
            print("Please enter an interger value")

print(f"Acceleration is {coefficients[0]}x^3 + {coefficients[1]}x^2 + {coefficients[2]}x \n Initial Velocity is {coefficients[3]}")

while True:
    try:
        st = float(input('Starting Time in Seconds: '))
        et = float(input('Ending Time in Seconds: '))
    except ValueError:
        print('Time value must be numerical')

    if et >= st:
        break
    else:
        print("The Start Time must be less than the End Time")

#CALCULATE THE DISTANCE from End Time - Start Time

End_Distance = ((coefficients[0]*et**4 / 4) + (coefficients[1]*et**3 / 3) + (coefficients[2]*et**2 / 2) + (coefficients[3]*et))
Start_Distance = ((coefficients[0]*st**4 / 4) + (coefficients[1]*st**3 / 3) + (coefficients[2]*st**2 / 2) + (coefficients[3]*st))

Distance_Covered = (End_Distance - Start_Distance)

print(f"\nDistance Covered: {Distance_Covered}\n")


def func(x):
    return ((coefficients[0]*x**4 / 4) + (coefficients[1]*x**3 / 3) + (coefficients[2]*x**2 / 2) + (coefficients[3]*x))


a, b = st, et  # integral limits
x = np.linspace(0, et + 10)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)


plt.show()