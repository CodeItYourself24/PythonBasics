# squares of numbers in a list
numbers = [1, 2, 3, 4, 5]
sqls = [i*i for i in numbers]
print(f"squares of numbers: {sqls}")

# print even numbers from 1-10
evls = [i for i in range(11) if i%2==0]
print(f"even numbers: {evls}")

# iterating through a str
sls = [i for i in 'Im a programmar']
print(f"looping througha str: {sls}")

# assigning integers 0 to 2 to 3 rows of the matrix
matrix = [[j for j in range(3)] for i in range(3)]
print(f"maxtrix integers: {matrix}")

# Reverse each string in a Tuple
stple = [i[::-1] for i in ('Im', 'python', 'programmar')]
print(f"reversing each str in a tuple: {stple}")

# list composed of odd numbers from 1 to 9.
odls = [i for i in range(10) if i%2==1]
print(f"odd numbers from 1-10: {odls}")

# all of the numbers from 1–1000 that are divisible by 8
diveight = [i for i in range(1001) if i%8==0]
print(f"numbers div by 8:{diveight}")

# all of the numbers from 1–1000 that have a 6 in them
iff_six = [i for i in range(1001) if '6' in str(i)]
print(f"six in range of 1001: {iff_six}")

# number of spaces in a string
strng = "Practice Problems to Drill List Comprehension in Your Head."
space_count = len([char for char in strng if char==' '])
print(f"space count in a strng: {space_count}")

# Remove all of the vowels in a string
vowels = ['a','i','e','o','u']
rem_vowels = [i for i in strng if i not in vowels]
print(rem_vowels)