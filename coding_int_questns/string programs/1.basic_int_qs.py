# Reverse a given string

s = 'jonsnow'
rs = s[::-1]    # negative slicing
print(rs)

nws = ''.join(reversed(s))  # using reversed func
print("using reversed func: ",nws)


# Count the number of spaces in a string

def count_Spaces(strng):
    count = 0
    for c in range(0,len(strng)):
        if strng[c] == " ":
            count +=1
    return count

strng = "this is a sample string"
print(f"number of spaces: {count_Spaces(strng)}")


# Remove all of the vowels in a string

vowels = ['a','e','i','o','u','A','E','I','O','U']
res = ""
for char in strng:
    if char not in vowels:
        res = res+char

print("removing the vowels: ",res)

# Create a string made of the first, middle and last character

a = "James"	
x=a[0]+a[len(a)//2]+a[-1]
print(x)

# Find the last position of a given substring

s1 = "Emma is a data scientist who knows Python. Emma works at google."
index = s1.rfind("Emma")
print("index of last pos of emma: ",index)