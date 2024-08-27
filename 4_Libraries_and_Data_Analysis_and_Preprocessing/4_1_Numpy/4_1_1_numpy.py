import numpy as np
arr = np.array([1,2,3,4,54,12,45,0,10])
print(arr)

print("max function", arr.max())
print("argmax function", arr.argmax())
print("min function", arr.min())
print("argmin function", arr.argmin())

print("zeros array",np.zeros(3))
print("zeros array 2d",np.zeros((3,3)))

print("ones array",np.ones(3))
print("ones array 2d",np.ones((3,3)))

print("linspace array",np.linspace(3,10,3))

print("Identical array",np.eye(4))

print("Random array",np.random.rand(5,5))

