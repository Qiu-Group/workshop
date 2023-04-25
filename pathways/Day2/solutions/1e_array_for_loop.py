import numpy as np
np.a = np.array([1, 2, 3])
np.b = np.array([4, 5, 6])
np.c = np.a + np.b
print(np.c)


#length of array np.c
size_c = len(np.c)

# example of a for loop
for i in range(size_c):
	print('Element', i , 'of array np.c is' , np.c[i]) 
