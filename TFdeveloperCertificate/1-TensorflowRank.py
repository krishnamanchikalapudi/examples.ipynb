import tensorflow as tf
import numpy as np

# Rank 0: Scalar (magnitude only)
s = 450
print(f"Rank: {tf.rank(s)} and shape: {np.shape(s)} for scalar: {s} ")

# Rank 1: Vector (magnitude and direction)
v = [3, 5, 6, 2]
print(f"Rank: {tf.rank(v)} and shape: {np.shape(v)}  for Vector: {v}")

# Rank 2: Matrix (table of numbers)
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Rank: {tf.rank(m)} and shape: {np.shape(m)}  for Matrix: {m}")

# Rank 3: 3-Tensor (cube of numbers)
t = [[[2], [4], [6]], [[8], [10], [12]], [[14], [16], [18]]]
print(f"Rank: {tf.rank(t)} and shape: {np.shape(t)}  for tensor {t}")