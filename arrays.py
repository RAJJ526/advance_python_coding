# # # one dimension structure
# # import numpy
# # a=numpy.array([1,2])
# # print(a.shape)

# import numpy
# a=numpy.array([1,2])
# print(a)

# # two dimension structure
# import numpy
# R=numpy.array([[2,3,4],[5,6,7], [8,9,2]])
# print(R[1][0])

# # # three dimension structure
# import numpy
# T=numpy.array([[[2,3,4],[3,4,5]],[[3,4,5],[6,7,8]]])
# print(T[1][1][2])

# import numpy as sp
# y=sp.array([[[2,3,4],[5,6,7]],[[6,7,8],[7,8,9]]])
# print(y [0] [1] [1])

# program show type of array
# import numpy
# a=numpy.array([1,2])
# print(a.ndim)
# print(a.shape)

# import numpy as lp
# x=lp.array([[4,5,6],[6,7,8]])
# print(x.ndim)
# print(x.shape)

# # import numpy
# # b=numpy.array([[2,3],[4,5],[6,7]])
# # print(b.ndim)
# # print(b.shape)

# # import numpy
# # c=numpy.array([[[2,3],[3,4],],[[4,5],[6,7]]])
# # print(c.ndim)
# # print(c.shape)

# #show type of array
# import numpy as train
# arr=train.array([1,2,3,4,5,6])
# print(type(arr))

# import numpy
# hit=numpy.array([[3,4,5],[5,6,7]])
# print(type(hit))

# import numpy as train
# delta=train.array([1,2,3,4,5,6])
# print(delta)

# #version of string
# import numpy as hit
# print(hit.__version__)

# import numpy
# print(numpy.__version__)

# #create a 0dimesional array
# import numpy
# x=numpy.array(24)
# print(x)

# #create any dimensional array
# import numpy as np
# arr = np.array([1, 2, 3, 4], ndmin=3)
# print(arr)
# print('number of dimensions :', arr.ndim)

# import numpy 
# arr=numpy.array([2,3,4,5], ndmin=6)
# print(arr)
# print(arr.ndim)

# import numpy
# arr=numpy.array([[1,2,3,4],[4,5,6,7]], ndmin=10)
# print(arr)
# print(arr.ndim)

# #slicing of array
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])

# import numpy
# bite=numpy.array([[2,3,4,9],[3,4,5,6],[7,8,9,0]])
# print(bite[1][0:3])

# import numpy
# arr=numpy.array([[[1,2,3],[3,4,5]],[[4,5,6],[6,7,8]],[[6,7,8],[8,9,0]]])
# print(arr.ndim)
# print(arr.shape)
# print(type(arr))
# print(arr[2][1][0:2])

# import numpy as np
# x=np.array([[[4,5,6]],[[6,7,8]],[[7,6,5]]])
# print(x[1] [0] [0:2])

# import numpy as np
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])

# #show index of element
# import numpy
# arr=numpy.array([[1,2,3,4],[4,5,6,7]])
# print(arr[0:2, 2]) 

# import numpy as np
# arr=np.array([[[3,4,5]],[[6,7,8]],[[7,8,9]]])
# print(arr [0:3,0:3,1])

# #return another array with slicing of two elements
# import numpy as np
# arr=np.array([[1,2,3,4],[4,5,6,7]])
# print(arr[0:2,1:3])

# #add two elements of array
# import numpy as op
# arr=op.array([1,2,3,4,5,6,7])
# print(arr[3]+arr[6])

# #show data type of array
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# print(arr.dtype)

# import numpy as np
# arr=np.array([3,4,5,6,7])
# print(arr.dtype)

# import numpy as np
# arr=np.array([1,2,3,4,44,55,5,6,7])
# print(arr.dtype)

# #show datatype of an array containing string
# import numpy
# arr=numpy.array(["the","fox","over", "the ","lazy","dog"])
# print(arr.dtype)

# #Create an array with datatype string
# import numpy as np
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)

# import numpy as np
# arr=np.array([3,4,5,6,9], dtype="f")
# print(arr)
# print(arr.dtype)

# import numpy as np
# arr=np.array([2,3,4,5,6],dtype='S')
# print(arr)
# print(arr.dtype)

# #change the datatype float to integer using "i"
# import numpy as np
# arr = np.array([1.5, 2.6, 3.7])
# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)

# import numpy
# arr=numpy.array([2.3,4.5,6.7])
# new=arr.astype("i")
# print(new)

# import numpy as np
# arr=np.array([2.3,5.4,7.9])
# new_arr=arr.astype("i")
# print(new_arr)

# #change the datatype from float to integer by using int and "N"
# import numpy as dp
# arr=dp.array([1.1,2.3,3.4,4.5])
# new_arr=arr.astype(int)
# print(new_arr)
# print(new_arr.dtype)

# #change the datatype from integer to boolean or float
# import numpy as sp
# arr=sp.array([1,2,0,4,5])
# new_arr=arr.astype(bool)
# print(new_arr)
# print(new_arr.dtype)

# import numpy as np
# arr=np.array([2,3,4,5,6])
# new_arr=arr.astype(float)
# print(new_arr)
# print(new_arr.dtype)

# #copy and change the original array
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)

# #copy of an array
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# x=arr.copy()
# print(x)

# #change the original array
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# arr[0],arr[4]=56,87
# print(arr)

# #make a view change the original array and display both array
# import numpy as sp
# arr=sp.array([1,2,3,4,5,6,7,8])
# x=arr.view()
# arr[0]=34
# arr[4]=65
# print(arr)
# print(x)

# import numpy as sp
# arr=np.array([1,2,3,4,5,6,7,8])
# x=arr.view()
# x[0]=34
# x[4]=65
# print(arr)
# print(x)

# import numpy as np
# arr=np.array([2,3,4,6,7,8,8,9])
# x=arr.view()
# arr[2]=45
# arr[4]=85
# print(x)

# #Print the value of the base attribute to check if an array owns it's data or not:
# import numpy
# arr=numpy.array([1,2,3,4,5])
# x=arr.copy()
# y=arr.view()
# print(x.base)
# print(y.base)

# #create an array of 5 dimension using ndmin
# import numpy as np
# arr=np.array([1,2,3,4,5], ndmin=5)
# print(arr)
# print(arr.shape)

# #convert the 1d array into 2d array
# import numpy as sp
# arr=sp.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_arr=arr.reshape(4,3)
# print(new_arr)

#convert the 1d array into 2d array
# import numpy as np
# arr=np.array([2,3,4,5,6,7,5,6])
# new=arr.reshape(2,2,2)
# print(new)

# #convert the 1d array into 3d array
# import numpy as sp
# arr=sp.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_arr=arr.reshape(2,3,2)
# print(new_arr)

# #convert 3d array into 2d array or 1d array
# import numpy as np
# arr=np.array([[[ 1 , 2],[ 3 , 4],[ 5,  6]],[[ 7 , 8],[ 9 ,10],[11 ,12]]])
# new_arr=arr.reshape(1,12)
# again_array=new_arr.reshape(4,3)
# print(again_array)

# #check if the returned array is a copy or a view
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(2,4).base)

# #converting multidimensional arrays into 1d array
# import numpy as np
# arr=np.array([[2,3,4,5,9],[4,5,6,7,8]])
# new_arr=arr.reshape(-1)
# print(new_arr)

# import numpy as np
# arr=np.array([[[2,3,4,5,9],[4,5,6,7,8]],[[2,3,4,5,7],[5,6,7,8,7]]])
# new_arr=arr.reshape(-1)
# print(new_arr)

# #irerating arrays
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

# #iterating two dimensional arrays
# import numpy as sp
# arr=sp.array([[1,2,3,4],[4,5,6,7]])
# for i in arr:
#   print(i)

# #iterate on each scalar element of the 2d array
# import numpy as dp
# arr=dp.array([[2,3,4,5],[5,6,7,8]])
# for i in arr:
#   for j in i:
#     print(j)

# #iterate on 3d array
# import numpy as kb
# arr=kb.array([[[3,4,5],[4,5,6]],[[5,6,7],[9,0,1]]])
# for i in arr:
#   print("i represent 2d array")
#   print(i)

# #to return the actual values that is scalar we have to iterate over each value
# import numpy as np
# arr=np.array([[[3,5],[5,6]],[[4,5],[7,8]]])
# for i in arr:
#   for j in i:
#     for k in j:
#       print(k)

# #program to print actual values using np.nditer
# import numpy as np
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for i in np.nditer(arr):
#   print(i)
  
# #iterate through the array as a string
# import numpy as np
# arr = np.array([1,2,3], dtype="S")
# for i in arr:
#   print(i)

# import numpy as np
# fkf=np.array([1,2,3], dtype="f")
# for i in fkf:
#   print(i)

# #combine two arrays
# import numpy as np
# arr1 = np.array([[5,6,7],[7,8,9]])
# arr2 = np.array([[4,5,6],[6,7,8]])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# import numpy as dp
# arr1=dp.array([1,2,3,4])
# arr2=dp.array([4,5,6,7])
# arr=dp.concatenate((arr1,arr2))
# print(arr)

# #join two 2d arrays along row(axis=1)
# import numpy as sp
# arr1=sp.array([[2,3],[4,5]])
# arr2=sp.array([[5,6],[7,8]])
# arr=sp.concatenate((arr1,arr2),axis=1)
# print(arr)

# #join two arrays using stack
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

# # NumPy provides a helper function: hstack() to stack along rows.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.hstack((arr1, arr2))
# print(arr)

# # NumPy provides a helper function: vstack()  to stack along columns.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.vstack((arr1, arr2))
# print(arr)

# # NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.dstack((arr1, arr2))
# print(arr)

# # Split the array in 3 parts:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr)

# # Access the splitted arrays:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# # Split the 2-D array into three 2-D arrays.
# import numpy as np
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)

# #split the 2d array into row direction
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr, 3, axis=1)
# print(newarr)

# #split along rows using hsplit method
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.hsplit(arr, 3)
# print(newarr)

# xnx  =   'xyx'

# py ='ooooo'

