import  pandas  as pd
import seaborn
import matplotlib
import numpy as np
##r w >
ML = print
print(pd.__version__)
print(seaborn.__version__)
print(matplotlib.__version__)
print(np.__version__)

myList = [1, 2, 3]
print(np.array(myList))
my__matix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(my__matix))
my__matix1 = [[4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(np.array(my__matix1))
print(np.arange(0, 101, 2))
print(np.zeros(5))
print(np.zeros((5, 5)))
print(np.ones(5))
print(np.linspace(0, 10, 3))
print(np.linspace(0, 10, 21))
print(np.eye(6))
print(np.random.rand(5, 6))
print("-------------------------------")
print(np.random.randn(10))
print(np.random.randn(2, 3))
print("-------------------------------")
print(np.random.randint(0, 101, 10))
print(np.random.seed(42))
print(np.random.rand(4))
print(np.random.seed(101))
print(np.random.rand(5))
Calculating_max = np.random.randint(0, 101, 10)
print(Calculating_max)
Max = Calculating_max.max()
Agmax = Calculating_max.argmax()
Min = Calculating_max.min()
print("-----------------------------")
print("Max-Value", Max)
print("Minimum-Value", Min)
print("AgMax-Value", Agmax)

oiginal_array = np.arange(12)
print(oiginal_array)
shape_array = oiginal_array.reshape(3, 4)
print(shape_array)

a1 = np.arange(0, 11)
ML(a1)
ML(a1[8])
ML(a1[1:5])
ML("", a1[:5])
a2 = a1[0:5] = 100
ML(a1)

a2 = np.arange(0, 11)
ML(a2)
Slice_of_a = a1[0:5]
ML(Slice_of_a)
m = Slice_of_a[:] = 99
ML(m)
ARRAY_COPY = a1.copy()
ML("Copy", ARRAY_COPY)
ARRAY_COPY[:] = 100
ML(a1)

ARR_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ML(ARR_2D)
ML(ARR_2D.shape)
ML(ARR_2D[:2, 1:])

##Condional ==============================
ML(ARR_2D > 4)
ML(a1[a1 > 4])

Numpy_List = [1, 2, 3]
ML(type(Numpy_List))
##r
ML(np.array(Numpy_List))
ML(type(Numpy_List))
ML(np.ndarray)
my__matix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ML(my__matix1)
ML(np.arange(0, 10))
ML(np.arange(0, 100, 2))
ML(np.zeros(5))
ML(np.ones(6))
ML(np.linspace(0, 10, 11))
ML(len(np.linspace(0, 5, 11)))
ML(np.eye(5))
ML(np.eye(7))
ML(np.random.rand(5, 2))
ML(np.random.randn)
ML(np.random.randn(2, 3))
ML(np.random.randint(0, 101, (4, 5)))
ML(np.random.seed(42))
ML(np.random.rand(4))
ML(np.arange(0, 25))
Reshape_1 = np.arange(0, 25)
ML(Reshape_1.reshape(5, 5))

randd = np.random.randint(0, 101, 10)
ML("Random_Maximum", randd.max())
ML("Random_Minimum", randd.min())
ML("Argment_Max", randd.argmax())
ML("Argment_Min", randd.argmin())
ML("Rana_dtype", randd.dtype)
shape_array1 = np.arange(25)
ML(shape_array1)
# ML(shape_array1.reshape(1, 5))

np_arr = np.arange(0, 11)
ML(np_arr)
ML(np_arr[8])
ML(np_arr[1:5])
ML(np_arr[:5])
ML(np_arr[5:])
np_a1 = np_arr[0:5] = 100
ML(np_arr)
slice_of_arr = np_arr[:] = 99
ML(np_arr)
np_arr_copy = np_arr.copy()
ML("copy of np_arr", np_arr_copy);
np_arr_copy[:]=10;
ML(np_arr_copy)

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]]);
ML(arr_2d);
ML(arr_2d.shape)
ML(arr_2d[1,1]);
ML(arr_2d[:2]);
ML(arr_2d[:2,1:]);

# Conditional Selection
C_selection_arr=np.arange(1,11);
ML(C_selection_arr);
ML(C_selection_arr>5);
Boolean_a=C_selection_arr[C_selection_arr>4];
ML(Boolean_a);




