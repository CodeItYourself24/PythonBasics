# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

add = lambda x: x+15
print("adding 15 using lambda: ",add(5))

mul = lambda x,y: x*y
print("mul x and y using lambda: ",mul(2,3))

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
'''Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75'''

def func(n):
    return lambda x:x*n
res = func(2)
print(f"double of 15: {res(15)}")

res = func(3)
print(f"triple of 15: {res(15)}")

# Write a Python program to sort a list of tuples using Lambda.
'''Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''

tup = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
tup.sort(key=lambda x:x[1])
print("sorting the tup using lambda: ",tup)


# Write a Python program to sort a list of dictionaries using Lambda.
'''Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]'''

dic = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dic.sort(key=lambda x:x['make'])
print(dic)

# Write a Python program to filter a list of integers using Lambda.
'''Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]'''
o_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = list(filter(lambda x:x%2==0, o_list))
print(f"even numbers: {even_num}")

odd_num = list(filter(lambda x:x%2!=0, o_list))
print(f"odd numbers: {odd_num}")

# Write a Python program to square and cube every number in a given list of integers using Lambda.
'''Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]'''

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq_num = list(map(lambda x: x**2,ls))
print(f"square of every number: {sq_num}")

cub_num = list(map(lambda x: x**3,ls))
print(f"cube of every number: {cub_num}")

# Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output: True/False
strng = "Python is to code"
strng1 = "PostgreSQL is to save data]"

starts_with = lambda x: True if x.startswith('P') else False
print(starts_with(strng))

