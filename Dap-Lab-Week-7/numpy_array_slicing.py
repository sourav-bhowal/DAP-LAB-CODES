import numpy as np  
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])  
print(a)  
print("After slicing")  
print(a[1:])  

# Another example  
print("\nOur array is:")  
print(a)  
print("The items in the second column are:")  
print(a[..., 1])  
print("\nThe items in the second row are:")  
print(a[1, ...])  
print("\nThe items column 1 onwards are:")  
print(a[..., 1:])  