'''
Write a program to solve:
X=log(x+1)
'''
import math

def iteration(value, max_iterations=100000):
    for i in range(max_iterations):
        next_iteration = math.log(value+1)
        value = next_iteration
    return value

print(iteration(1))