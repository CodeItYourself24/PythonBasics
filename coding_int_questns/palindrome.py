# Write a program to check if the given number is palindrome or not.

def is_palindrome(number):
    num_str = str(number)   # converting a number into str for easy reversal
    if num_str == num_str[::-1]:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")