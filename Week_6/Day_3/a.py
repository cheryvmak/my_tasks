import numpy as np

def numpy_2D(a):
    result = a.copy()
    result = np.where(a % 2 == 0, a ** 2, -1)
    return result


rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))

if rows <= 0  or columns <= 0:
        raise ValueError
input_array = []
print(f"Enter {rows * columns} integer for {rows} x {columns} array (row by column)")
for i in range (rows):
    rows = []
    for j in range (columns):
        while True:
            try:
                element = input(f"Enter element at position {i}{j}:")
                input_array.append(element)
                break
            except ValueError:
                print("Please enter a valid integer")
                input_array.append(rows)

a = np.array(input_array, dtype=np.int64)
output = numpy_2D(a)
print(output)
