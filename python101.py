import pandas as pd
import numpy as np

#online compilers
#https://www.onlinegdb.com/online_python_compiler
#https://www.online-python.com/
#https://www.programiz.com/python-programming/online-compiler/


#print, and printing two or more elements: ,
# print('value' , 6)
#comment


#variables
minagin = 5
string = 'string'
miangin_ye_seri_adad =5
# no need to define type of variables(float, integer, string)
#right name for variables , use _ for space , this_is_var = 5
#rewrited variable will lose its initial value,  example: changing values of two variables
var = 5
var = 6
print(var)



#array(list)

array = []
array1 = [1,3,6,'hi']

#counting arrays: 0, 1, 2 ...
#reading values, elements of the array
#len method
# print(array1[-1])
# print(len(array1))



#reading negatives, and accessing specific period:x[-1] , x[1:3] , x[:4] , x[4:] , x[1:3] , x[-1] , x[-4:-1]
# print(array1[-4:-1])



#adding array's elements with append method
array1.append(6)

#changing array with var[i] method
array1[1] = 'change'


#deleting elements in array, pop, del method
array1.pop(0)
# del var[0]
del array1
# print(array1)

#deleting the whole array

# var.clear()

### sort method

var = [5,6,5,10,6]
var.sort()
var.reverse()
# print(var)

# #dictionary
dict = {}
dict = {'value' : var,
'another value' : var[2],
var[1]: var[3]
}
#reading dictionary elements
# print(dict['value'])

#general reading with keys() method, reading with values() method

# print(dict.keys())
# print(dict.values())

#reading an element


#changing an element
dict['value'] = 5
# print(dict)


#adding to dictionary
dict['new'] = 66

#deleting an element and whole dictionary .pop() .clear()
dict.pop('value')
# print(dict)


#adding arrays : var1 + var2
x=5
y=6
xi = [1,3,50]
yi = [6,8,9]
# print(x,y) 






#input 

# inputs = input('enter the data')
# print(inputs)
#default type is string, changing to integer
# input_var = int(input('insert input'))

# print( input_var+5)


#if
#else and elif in python
# h = False
# if (h==False):
#  print('ok')
# elif(h==False):
#     print('if it was something specific')
# else:
    # print('anything but false')

# there is no {} in python, scope of loops, ifs, whiles, functions... is determined by space

# operators: ==(difference between = and ==), != , > , < , >= , <= , or , and


#if in dataset

# if (5 in var):

#  print('5 in var')






#for, for in dataset, range() 
# for i in range(10):
#  print(i)
# for i in var :
#     print(i)
##while
# print(h)
# while h==False:
#     print('ok')
#     h=True
#nested loop(loop inside loop)
#looping through all j(s) for each i
for i in range(10):
    for j in range(5):
        print(i,j)
##flag
# flag=True
# while(flag==True):
    # x=int(input('insert number'))
    # if(x==0):
        # flag=False


#libraries, importing and installing, using PIP ( how and where to import them)

#numpy , pandas ,matplotlib
#random numbers
#numpy ( numerical python)=> pip install numpy

# print(np.random.choice([2,6,5,8]))
#np.arange
# print(np.random.choice(np.arange(1,1000)))
#with P
# print(np.random.choice([1,2,4,5,9],p=[0.4,0.3,0.1,0.1,0.1]))
#various distributions
# print(np.random.normal(loc=5,scale=3))
#search for other distributions



#pandas (analyzing data, defining dataset, reading, writing excel files, and plotting)=> pip install pandas
#write excel file
var = [5,6,9,7,2]

dataset = {
    'value1': var,
    'value2' :'data'
}
import pandas as pd
df = pd.DataFrame(dataset)
# print(df)
#df.to_csv('E:\\winrar\excel.csv')

#reading excel file
df = pd.read_csv('E:\\winrar\excel.csv')

#visualizing data using matplotlib=> pip install matplotlib
# import matplotlib.pyplot as plt
# df.plot()
# plt.show()







##function
# def myfunc():
    # return(5)
# print(myfunc())

#with arguments

# def func(number):
#     return(number + 5)
# print(func(5))







#sources:
#stackoverflow for errors
#geeksforgeeks for errors
#w3schools.com for methods and references

#debugging:
#search bugs and errors in either youtube or google search
# codes at: https://github.com/deDg0d/Simulation-via-python





