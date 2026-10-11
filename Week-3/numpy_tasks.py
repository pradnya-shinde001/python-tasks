import numpy as np

#### Task 1. Create a vector from 10 to 49 and reverse it
a = np.arange(10, 50)
print("Original:", a)

reversed_a = a[::-1]
print("Reversed:", reversed_a)

#### Task 2. Create a random 5 × 5 array and find its minimum and maximum

b = np.random.random((5, 5))

print(b)
print("Minimum:", b.min())
print("Maximum:", b.max())

#### Task 3. Normalize a 5 × 5 random matrix

c = np.random.random((5, 5))

minimum = c.min()
maximum = c.max()

if maximum != minimum:
    normalized = (c - minimum) / (maximum - minimum)
else:
    normalized = np.zeros_like(c)

print("Original matrix:\n", c)
print("Normalized matrix:\n", normalized)

#### Task 4. Multiply a 5 × 3 matrix by a 3 × 2 matrix

A = np.random.randint(1, 10, size=(5, 3))
B = np.random.randint(1, 10, size=(3, 2))

C = A @ B

print("A shape:", A.shape)
print("B shape:", B.shape)
print("Result shape:", C.shape)
print(C)

#### Task 5. Get yesterday's, today's and tomorrow's dates

today = np.datetime64("today", "D")

yesterday = today - np.timedelta64(1, "D")
tomorrow = today + np.timedelta64(1, "D")

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#### Task 6. Extract the integer part using five methods

import numpy as np

d = np.random.uniform(-5, 5, size=10)
print("Original:", d)

print("1. astype:", d.astype(int))
print("2. floor:", np.floor(d))
print("3. trunc:", np.trunc(d))
print("5. integer division:", np.trunc(d / 1).astype(int))


#### Task 7. Create a structured array representing a position (x,y) and colour (r,g,b)

dtype = [
    ("x", float),
    ("y", float),
    ("r", np.uint8),
    ("g", np.uint8),
    ("b", np.uint8)
]

points = np.array([
    (1.5, 2.5, 255, 0, 0),
    (3.0, 4.0, 0, 255, 0),
    (5.0, 6.0, 0, 0, 255)
], dtype=dtype)

print(points)
print("X coordinates:", points["x"])
print("Y coordinates:", points["y"])
print("RGB colours:", points[["r", "g", "b"]])


#### Task 8. Use a generator to generate 10 integers and build an array

def generate_numbers():
    for i in range(10):
        yield i

a = np.fromiter(generate_numbers(), dtype=int)

print(a)


#### Task 9. Check whether two random arrays are equal

A = np.random.random((3, 3))
B = np.random.random((3, 3))

print("A:\n", A)
print("B:\n", B)

print("Element-wise equality:\n", A == B)
print("Completely equal:", np.array_equal(A, B))

#### Task 10. Consider a random vector with shape (100, 2)
# representing coordinates, find point-to-point distances

points = np.random.random((100, 2))

distances = np.linalg.norm(points, axis=1)

print("Coordinates:\n", points)
print("Distances from origin:\n", distances)


#### Task 11. Subtract the mean of each row of a matrix

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=float)

row_means = A.mean(axis=1, keepdims=True)
result = A - row_means

print("Row means:", row_means.ravel())
print(result)

#### Task 12. Sort an array by its nth column

A = np.array([
    [4, 30, 2],
    [1, 10, 5],
    [3, 20, 1]
])

n = 1  # Sort by the second column

sorted_A = A[A[:, n].argsort()]

print(sorted_A)


#### Task 13. Compute a matrix rank

rank = np.linalg.matrix_rank(A)

print("Matrix rank:", rank)

#### Task 14. Consider a 16 x 16 array, how to get the block-sum (block size is 4 x 4)?

A = np.arange(16 * 16).reshape(16, 16)

block_sums = A.reshape(4, 4, 4, 4).sum(axis=(1, 3))

print("Original shape:", A.shape)
print("Block sums:\n", block_sums)
print("Result shape:", block_sums.shape)



