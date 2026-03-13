"""
# que: rev list useing stack
stack = [10, 20, 30]
rev_stack = []

for i in range(len(stack)):
    rev_stack.append(stack[-1])
    stack.pop()

print(rev_stack)
"""
"""

# que: check if paranthesis are balanced or not

que = "){}"

def check_valid(que) -> bool:
    stack = []
    if not que:
        return True
    for c in que:
        if c in "[{(":
            stack.append(c)
        else:
            if not stack and c in ")}]":
                return False
            top = stack[-1]
            if top == "(" and c == ")" or top == "{" and c == "}" or top == "[" and c == "]":
                stack.pop()
            else:
                return False
    if len(stack)>=1 :
        return False
    else:
        return True

print(check_valid(que))
"""

"""
# que: find the Next Greater Element (NGE) for each element in the array. If no such element exists, use -1.

arr = [4, 5, 2, 10, 8]
ans = [-1]*len(arr)
stack = []
for i in range(len(arr)-1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1]
    stack.append(arr[i])
print(ans)
"""


# Q. You are given an array of heights representing a histogram, where each bar has width 1. Find the area of the largest rectangle that can be formed in the histogram.

# heights = [2, 1, 5, 6, 2, 3]
# ans = 10


"""
nums = [3,3]
target = 6
seen = {}

def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return None
"""


nums = [2,15,11,7] # unsorted array
target = 9

hashmap = {}

for i, n in enumerate(nums):
    if target-n in hashmap:
        print(hashmap[target-n], i)
    else:
        hashmap[n] = i

