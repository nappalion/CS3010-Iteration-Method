'''
Write a program to solve:
X+Y=e^(-X-Y)

z=0.567
y=-0.433
x=1
'''
import math

z = math.exp(1)
for i in range(50):
    print(z)
    z = math.exp(-z)