# Machine Learning Week 2 Practical Exercises
# Author: Jordan Ung <jordanu107@gmail.com>
# Last Updated: 4/3/19

# Homogenous multidimensional array - less flexible than a list or tuple
# but faster in mathematical computations - ref to. numpy object
import numpy as np 
import matplotlib as mpl
import sklearn

#arrays created using arange method - similar to range for lists
####a = np.arange(5) - > array([0, 1, 2, 3, 4])
####b = np.array([1, 3, -2, 0, 0])
####a + b -> array([1, 4, 0, 3, 4])

# Function to calculate Euclidean Distance between two arrays (2b)
# In built way to find Euclidean Distance is np.linalg.norm(a, b)
def my_euclidean_dist(a, b):
	if (len(a) != len(b)):
		raise ValueError('The dimensions of a and b are not the same.')
	else:
		sum = 0
		for i in range(len(a)):
			sum += pow((a[i] - b[i]), 2)
		return pow(sum, 0.5)

