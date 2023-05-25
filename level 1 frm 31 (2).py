#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [1, 2, 5, 6]
res = [(val, pow(val, 3)) for val in list1]
print(res)


# In[2]:


Dict = {'Ram': 10, 'Ravi': 9,
        'John': 15, 'Sri': 2, 'Sita': 32}
 
Keys = list(Dict.keys())
Keys.sort()
sorted_dict = {i: Dict[i] for i in Keys}
 
print(sorted_dict)


# In[3]:


import random as rn
dict = {}
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;
print(dict)


# In[4]:


def returnSum(Dict):
    list = []
    for i in Dict:
        list.append(Dict[i])
    final = sum(list)
    return final
dict = {'a': 10, 'b': 20, 'c': 30}
print("Sum :", returnSum(dict))


# In[5]:


import sys
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"name1": "Raj", "name2": "Nikhil", "name3": "Deepa"}
dic3 = {1: "zebra", 2: "Tiger", 3: "Fox", 4: "tiger"}
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")


# In[6]:


test_set = set("Hello")
for val in test_set:
    print(val)


# In[10]:


def Max(sets):
    return (max(sets))
sets = set([8, 16, 24, 1, 25, 30, 100, 65, 85])
print(Max(sets))


# In[ ]:


def min(sets):
    return(min(sets))
sets = set([2,5,7,3,9,20])
print(min(sets))


# In[6]:


list=['apple','orange','strawberry']
list.remove('orange')
print(list)


# In[3]:


list1=[1,2,3,4]
list2=[5,6,3,1]
for i in list1:
    for j in list2:
        if list[i]==list[j]:
            print("The common element is",i)
            break
            


# In[1]:


s={1,2,3,4,5}
p={5,6,7,8,9}
for i in s:
    for j in p:
        if i==j:
            print("the common element is", i)


# In[2]:


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("the matrix is:")
for i in range(1, len(matrix)):
    matrix[i] = matrix[0]
print(matrix)


# In[3]:


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()


# In[4]:


elements = [1, 2, 3, 2, 1, 3, 4, 5, 4, 5, 5]
element_counts = {}
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
num_rows = max(element_counts.values())
num_cols = len(element_counts)
matrix = [[None] * num_cols for _ in range(num_rows)]
for col, element in enumerate(element_counts):
    count = element_counts[element]
    for row in range(count):
        matrix[row][col] = element
for row in matrix:
    print(row)


# In[5]:


matrix = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9))
row_sums = [sum(row) for row in zip(*matrix)]
print("Row-wise sums:")
for sum_value in row_sums:
    print(sum_value)


# In[6]:


def create_even_submatrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = 1
    return matrix
n = 4
result = create_even_submatrix(n)
for row in result:
    print(row)


# In[7]:


import inspect

def my_function(guna,dinesh, kannan):
    pass

parameters = inspect.signature(my_function).parameters
parameter_names =list(parameters.keys()

print(parameter_names)


# In[8]:


name = "riya"
age = 28
city = "New York"

print(name, age, city)


# In[9]:


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

base =int(input("Enter the base: "))
exponent =int(input("Enter the power: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")


# In[20]:


class grade:
    def _init_(self, a, b):
        self.a = a
        self.b = b
  
    def _repr_(self):
        return str((self.a, self.b))
  

g= [grade("riya", 'a'),
       grade("diya", 'b'),
       grade("tanvi", 'c'),
       grade("shalu", 'd'),
       grade("miya", 's')]
  

print(sorted(g, key=lambda x: x.b))


# In[21]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="riya", age=18, city="chennai")


# In[ ]:




