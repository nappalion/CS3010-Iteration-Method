'''
Write a program to solve:
X=e^-x
'''
import math

def iteration(value, max_iterations=100000):
    for i in range(max_iterations):
        next_iteration = math.exp(-value)
        value = next_iteration
    return value

print(iteration(1))