# Variables in Python
first_name = 'rohit'
last_name = 'bugade'
country = 'india'
city = 'pune'
age = 18
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'rohit',
   'lastname':'bugade',
   'country':'india',
   'city':'pune'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
# print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'rohit'
print(first_name)               # 'rohit'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['r', 'o', 'h', 'i', 't']

n=8
m=float(n)
print(m)
