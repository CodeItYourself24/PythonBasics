'''Given a list of numbers and a number k, write a Python program to check whether the sum of any two numbers from the list is equal to k or not.'''

def check_sum(nums,k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == k:
                return True
    return False
    
print(check_sum([1,2,3,4,5],70))

# pairs that adds upto k

def find_pairs(nums, k):
    pairs = []
    seen = set()

    for num in nums:
        diff = k - num
        if diff in seen:
            pairs.append((num, diff))
        seen.add(num)

    return pairs

numbers = [1, 2, 3, 4, 5, 6]
target_sum = 7
result = find_pairs(numbers, target_sum)
print(f"Pairs that add up to {target_sum}: {result}")