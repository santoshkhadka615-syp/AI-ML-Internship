# Week 2 - NumPy Exercises
# Covers: array creation, indexing, broadcasting, vectorized operations
# Run this file top to bottom, or copy pieces into a notebook cell by cell.

import numpy as np

# ---------- ARRAY CREATION ----------

# from a plain Python list
a = np.array([1, 2, 3, 4, 5])
print("From list:", a)

# array of zeros / ones
zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
print("Zeros:\n", zeros)
print("Ones:\n", ones)

# a range of numbers, like Python's range() but returns an array
range_arr = np.arange(0, 10, 2)  # start, stop, step
print("Arange:", range_arr)

# evenly spaced numbers between two values
linspace_arr = np.linspace(0, 1, 5)  # 5 numbers between 0 and 1
print("Linspace:", linspace_arr)

# random numbers (useful for quick testing)
random_arr = np.random.randint(1, 100, size=5)
print("Random ints:", random_arr)

# reshape a 1D array into a 2D grid
grid = np.arange(12).reshape(3, 4)
print("Reshaped 3x4:\n", grid)


# ---------- INDEXING & SLICING ----------

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Last element:", arr[-1])
print("First three:", arr[:3])
print("Every other:", arr[::2])

# 2D indexing: [row, column]
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at row 1, col 2:", matrix[1, 2])
print("Whole second row:", matrix[1, :])
print("Whole first column:", matrix[:, 0])

# boolean indexing - select values that meet a condition
nums = np.array([5, 12, 8, 20, 3, 17])
print("Numbers greater than 10:", nums[nums > 10])

# modify values using a condition
nums_copy = nums.copy()
nums_copy[nums_copy > 10] = 0
print("After zeroing values > 10:", nums_copy)


# ---------- BROADCASTING ----------
# broadcasting lets NumPy apply an operation between arrays of different
# shapes without writing a loop.

vector = np.array([1, 2, 3])

# add a single number to every element
print("Vector + 10:", vector + 10)

# add two arrays of the same shape
vector2 = np.array([10, 20, 30])
print("Vector + Vector2:", vector + vector2)

# adding a row vector to a matrix - the row gets applied to every row
matrix2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
row = np.array([10, 20, 30])
print("Matrix + row (broadcast):\n", matrix2 + row)

# adding a column vector - gets applied to every column
column = np.array([[100], [200], [300]])
print("Matrix + column (broadcast):\n", matrix2 + column)


# ---------- VECTORIZED OPERATIONS ----------
# doing math directly on whole arrays instead of looping element by element

prices = np.array([100, 250, 75, 300])

# apply a 10% discount to everything at once
discounted = prices * 0.9
print("Discounted prices:", discounted)

# elementwise operations between two arrays
quantities = np.array([2, 1, 5, 3])
totals = prices * quantities
print("Total per item:", totals)
print("Grand total:", totals.sum())

# built-in stats, no loops needed
print("Average price:", prices.mean())
print("Max price:", prices.max())
print("Min price:", prices.min())
print("Standard deviation:", round(prices.std(), 2))

# compare vectorized vs a manual loop (just to see why we use NumPy)
big_array = np.arange(1_000_000)

# vectorized way
squared_vectorized = big_array ** 2

# manual loop way (much slower for large arrays, kept small here as a demo)
small_array = big_array[:5]
squared_loop = []
for n in small_array:
    squared_loop.append(n ** 2)
print("Loop result (first 5):", squared_loop)
print("Vectorized result (first 5):", squared_vectorized[:5])