#Linear Search is a simple algorithm that looks for a target value in a list by checking each element one by one.
#Linear Search Overview
#How it works?
#1. You start from the first element and check if it's equal to the target value.
#2. if it matches, you return the index.
#3. If it doesn't, yo move to the next element and repeat until you either find the target or go through the entire list.
#Time Complexity:
#O(n): In the worst case, you may need to check all n elements in the list.
#Space Complexity
#O(1): Only a small, fixed amount of memory is used (just a few variables for looping and the result).

#A simple implementation of Linear Search in Python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   #Return the index of the Target
        return -1 #Target not found

#Example usage
arr = [5, 3, 8, 6, 7, 2, 9]
target = 7

result = linear_search(arr, target)
if result != -1:
    print(f"Target {target} was found at index {result}")
else:
    print(f"Target {target} was not found.")