""""
Example 1:
Input: nums = [2,7,11,15], target = 9

Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

def print_numbers(n):
    if n == 0:
        return
    
    print_numbers(n - 1)
    print(n)

print_numbers(5)

"""

def countdown(n):
    print(n)
    if n == 1:
        print("kabooomm")
        return 1
    
    n -= 1
    countdown(n)

countdown(10)