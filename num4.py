'''
Write a program to solve:
X=Sin(x+𝜋/4)
'''
import math

def iteration(value, max_iterations=100000):
    for i in range(max_iterations):
        next_iteration = math.sin(value + math.pi/4)
        value = next_iteration
    return value

print(iteration(1))