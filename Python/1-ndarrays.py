import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([[1, 2],
              [3, 4]])
d = np.array([[1, 2, 3],
              [4, 5, 6]])
e = np.array([10, 20, 30])

print(a + b)
print(a * b)

print('c:')
print(c)
print(f'a.sum(axis=0): {c.sum(axis=0)}')
print(f'a.sum(axis=1): {c.sum(axis=1)}')

print(f'd+e:\n', d + e)

