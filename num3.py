'''
Write a program to solve:
X=Sin(x)
'''
import math

def iteration(value, max_iterations=100000):
    for i in range(max_iterations):
        next_iteration = math.sin(value)
        value = next_iteration
    return value

print(iteration(1))