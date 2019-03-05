# Machine Learning Week 2 Practical Exercises
# Author: Jordan Ung <jordanu107@gmail.com>
# Last Updated: 4/3/19

# Homogenous multidimensional array - less flexible than a list or tuple
# but faster in mathematical computations - ref to. numpy object
import numpy as np
import matplotlib as mpl
import sklearn
import math


# arrays created using arange method - similar to range for lists
####a = np.arange(5) - > array([0, 1, 2, 3, 4])
####b = np.array([1, 3, -2, 0, 0])
####a + b -> array([1, 4, 0, 3, 4])

# Function to calculate Euclidean Distance between two arrays (2b)
# In built way to find Euclidean Distance is np.linalg.norm(a, b)
def my_euclidean_dist(a, b):
    if len(a) != len(b):
        raise ValueError('The dimensions of a and b are not the same.')
    else:
        sum = 0
    for i in range(len(a)):
        sum += pow((a[i] - b[i]), 2)
    return pow(sum, 1.0 / len(a))

# Function to calculate Hamming Distance between two arrays (2c)
def hamming_dist(a, b):
    if len(a) != len(b):
        raise ValueError('The dimensions of a and b are not the same.')
    else:
        sum = 0
    for i in range(len(a)):
        str1 = str(a[i])
        str2 = str(b[i])
        for j in range(len(str1)):
            if str1[j] != str2[j]:
                sum += 1
    return sum

# a = [0, "cat", 800, "??"]
# b = [1, "dog", -266, "??"]
#
# print(hamming_dist(a, b))

# Function to find the dot product between two vectors (3a)
def dot_product(a, b):
    product = 0
    for i in range(len(a)):
        product += a[i] * b[i]
    return product

print(dot_product([1,2], [1,1]))

def calculate_cos_angle(a, b):
    numerator = dot_product(a, b)
    denominator = my_euclidean_dist(a, np.array[0, 0]) \
                  * my_euclidean_dist(b, np.array[0, 0])
    angle = math.acos(numerator / denominator) # Returns in radians
    return angle * 180 / math.pi

print(calculate_cos_angle([1,2], [1,1]))