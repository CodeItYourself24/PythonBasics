'''Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not.'''

def check_sum(nums,k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == k:
                return True
    return False
    
print(check_sum([1,2,3,4,5],70))