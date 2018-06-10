import numpy as np;



print('-- Start --')


# a large array  , perform operation on all elements without looping

large_int_array = np.arange(1000)
print(large_int_array)

large_int_array_multiply_2 = np.array( [ x for x in large_int_array])
print(large_int_array_multiply_2)

print('-- cast int array to float  -- ')
large_int_array = large_int_array.astype(np.float64)
large_int_array = np.array( [ np.sqrt(x) for x in large_int_array])
print(large_int_array)


print('-- create multi d array -- ')
arr_2by3 = np.random.randn(2, 3)
print(arr_2by3)
print(arr_2by3[0][2])
print(arr_2by3.dtype)
print(arr_2by3.shape)
print(arr_2by3*arr_2by3)


print('-- pick out specific subsection of 2 d array  --')
arr_4by5 = np.random.randn(4,5)
print(arr_4by5)
# any operation on array is done on all elements and result is another array
print(arr_4by5 > 0)
# 1: means all rows/columns with index 1 and above
# :1 means one row or col
print('--  arr_4by5[1:] --')
print(arr_4by5[1:])

print('--  boolean indexing  --')

random_arr_5by5 = np.random.randint(2,10, size=(5,5) );
random_arr2_5by5 = np.random.randint(2,10, size=(5,5) );

print(random_arr_5by5)
print(random_arr2_5by5)
## compare each element of array to corresponding element (same co-ordinates) and put the result
## in boolean array of same dimension
print(random_arr_5by5 > random_arr2_5by5)


print('--  print only rows 4 ,2 ,3 in that order   --')
print(random_arr_5by5[[4,2,3]])

# arr[[1, 5, 7, 2], [0, 3, 1, 2]]  picks selected rows from arr , then picks selected
# elements from each row based on  column indices from second argument
# if arr is 2d array , gets (1,0)  , (5,3) ....


print('--  transpose   --')
print(random_arr_5by5)
print(random_arr_5by5.T)

print('--  mesh grid  --')

arr1d_1 = np.array([1,2,3,4,5])
arr1d_2 = np.array([6,7,8,9])

xx , yy = np.meshgrid(arr1d_1 , arr1d_2)

print(xx)

print(yy)

print(xx+yy)



print()
print('--   --')

print('-- End --')
