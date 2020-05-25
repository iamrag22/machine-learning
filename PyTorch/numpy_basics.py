import numpy as np 
print(np.__version__)

# Create array
a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])

def describe_array(a):
    print(a)
    print("Dimensions ", a.ndim)
    print("Shape ", a.shape)
    print("Number of elements ", a.size)
    print("Data type ", a.dtype)
    print("Total size in bytes ", a.nbytes)

# describe_array(a) # id array
# describe_array(b) # 2d array

def slicing_operations():
    print("Slicing operations")
    a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print(a[0, :])  # Print all  from a given row. Notice the comma
    print(a[:, 2])  # Print 2 nd col from all rows
    print(a[0:2, 2]) # For Rows 0 and 1 , print 2 column values [3,6]

    # Update all rows 1 st col
    a[:, 1] = 100
    print(a)

    #update all colmuns, 1st row
    a[1,:] = 200
    print(a)

slicing_operations()

def array_init():
    print("Array initialization")
    # Initialize arrays
    print(np.zeros((3,4)))  # The shape param should be a tuple
    print(np.ones((2,3)))
    print(np.full((2,4), 9))  # fill all rows and cols in shape with a default val

    def foo(x,y):
        return x+y

    # Fill an array of shape based on the function
    a = np.fromfunction(foo, (3,4))
    print(a)

array_init()


def binaray_operations():
    print("Binary operations")
    # Operations
    a = np.arange(4)
    b = np.array([1,2,3,4])

    # Binary
    print(a+b)  # Add
    print(b-a)  # Subtract
    print(a**2) # Power
    print(a*b)  # Multiply

    # DotProduct
    a = np.arange(4).reshape(2,2)
    b = np.arange(4).reshape(2,2)
    print(a.dot(b))

    # Check if 2 arrays have identical values
    a = np.array([1,2,3])
    b = np.array([1,2,4])
    print(a==b)
binaray_operations()

def unary_operations():
    # Unary Operations
    print("Unary operations")
    a = np.arange(12).reshape(3,4)
    print(a)
    print(a.sum())  # Sum of all elements in the matrix
    print(a.sum(axis=0)) #  Calculate per column sum
    print(a.sum(axis=1)) #  Calculates per row sum
    print(a.cumsum(axis=1)) # Runnning sum per row. Same shape as input

    # Check if each value satifies a condition
    a = np.arange(5)
    print(a%2==0)  # Returns if each el is even or odd

unary_operations()

def change_structure_operations():
    print("Reshape operations")
    a = np.arange(4).reshape(2,2) 
    print(a)

    # Transpose
    print(a.T)

    # Flatten a nd array to 1d
    b = a.ravel()
    print(b)

    # Resize (Modifies org array and does not return a copy)
    # Reshape returns a copy
    a = np.full((4,6), 7)
    print("Before resize ", a)
    a.resize((3,8))
    print("After resize ", a)

change_structure_operations()


def copy_operations():
    print("Copy operations")
    # No copy
    a = np.ones((2,3))
    b =a # b is a
    print(a is b)

    # View or shallow copy. Changes in 1 updates other
    c = a.view()
    c[1,2]= 100
    print(a)
    print(c)

    # Deep copy
    d = a.copy()
    print(d is a)
    d[1,2] = 1000
    print(a)
    print(d)
copy_operations()


a =np.eye(2)[0]
b =np.eye(2)[1]
print(a, b)