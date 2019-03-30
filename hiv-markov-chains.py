#-----
# This program was created for solving a problem presented 
# in the list of exercises (1) of my Computational Linear Algebra class.
#-----
import numpy as np
from numpy.linalg import matrix_power

#adjusting matrix printing settings
np.set_printoptions(precision=3, suppress=True)

#matrix with transition probabilities
stochastic_matrix = np.array([[0.9, 0.07, 0.02, 0.01], 
                              [0,   0.93, 0.05, 0.02], 
                              [0,   0,    0.85, 0.15], 
                              [0,   0,    0,     1.0]])

#initial state vector
pi_vector = np.array([0.85, 0.10, 0.05, 0.00])

#number of years to be computed
n = int(float(input("Number of years:")))

#compute final the final state of the pi_vector
final_state = pi_vector @ matrix_power(stochastic_matrix, n)

#print the result
print("\nFinal state  vector:\n", final_state)