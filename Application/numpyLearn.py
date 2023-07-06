# https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=numpy_tf2-colab&hl=en#scrollTo=hfYVa8iQTaUL

import numpy as np

one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)
sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

random_between_50_and_100 = np.random.randint(low=50, high=100, size=6)
print(random_between_50_and_100)

random_floats_between_0_and_1 = np.random.random([6]).round(decimals=2)
print(random_floats_between_0_and_1) 

# Task 1:
feature = np.arange(6, 21)
label = 3*feature + 4
# Task 2:
noise = (np.random.random([15]) * 4) - 2
noise = noise.round(decimals=1)
print(noise)
label = label + noise 
print(label)