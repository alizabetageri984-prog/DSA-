#Question 1 (basic): Given numbers = [1, 3, 5, 7, 9, 11, 13], find the index of target = 13 using binary search. Do a quick trace: what's left, right, middle at each step?



def binary_search(numbers, target):
    left_pointer = 0 
    right_pointer = len(numbers) - 1
    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2
        if numbers[middle_pointer] == target:
            return middle_pointer
        elif numbers[middle_pointer] < target:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1
print(binary_search([1, 3, 5, 7, 9, 11, 13], 13))
#Question 2 (edge case): What happens if target isn't in the list at all — say target = 6 in the same list? At what point does the loop stop, and what should we return?
def binary_search(numbers, target):
    left_pointer = 0 
    right_pointer = len(numbers) - 1
    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer)// 2
        if numbers [middle_pointer] == target:
            return middle_pointer
        elif numbers[middle_pointer] < target:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1
    return -1  # Target not found
print(binary_search([1, 3, 5, 7, 9, 11, 13], 6))
#Question 3 (conceptual) — we still haven't covered: why does Binary Search require the list to be sorted? What would break if you ran it on an unsorted list? Want to tackle that one now?
def binary_search(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) -1
    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer)// 2
        if numbers[ middle_pointer] == target:
            return middle_pointer
        elif numbers[middle_pointer] < target:
            left_pointer = middle_pointer + 1
        else:
            right_pointer = middle_pointer - 1
    return -1 #target not found
print(binary_search([1, 5, 3, 7, 9, 13, 11], 3)) #this will return -1 becuase the list is not sorted, and the binary search algorithim will not be able to find the target correctly.

class Solution:
    def search(self, nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if nums[middle_pointer] == target:
                return middle_pointer
            elif nums[middle_pointer] < target:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1
        return -1

print(Solution().search([-1, 0, 3, 5, 9, 12], 9))   # expect 4
print(Solution().search([-1, 0, 3, 5, 9, 12], 2))   # expect -1
#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

#Example 1:

#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4
#Example 2:

#Input: nums = [-1,0,3,5,9,12], target = 2
#Output: -1
#Explanation: 2 does not exist in nums so return -1
class Solution(object):
    def search(self, nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if nums[middle_pointer] == target:
                return middle_pointer
            elif nums[middle_pointer] < target:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1
        return -1

#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.


#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2
#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1
#Example 3:
#Input: nums = [1,3,5,6], target = 7
#Output: 4
class Solution(object):
    def searchInsert(self, nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if nums[middle_pointer] == target:
                return middle_pointer
            elif nums[middle_pointer] < target :
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1
        return left_pointer
#You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

#You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

    # The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left_pointer = 1
        right_pointer = n
        while left_pointer < right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2
            if isBadVersion(middle_pointer):
                right_pointer = middle_pointer

            else:
                left_pointer = middle_pointer + 1
        return right_pointer
#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.
class Solution(object):
    def searchRange(self, nums, target):
        left_pointer=0          #Start searching from index 0.
        right_pointer = len(nums) - 1# searching till  last index 
        first = -1    # - 1 is invalid index best way to tell that we noto found

        while left_pointer <= right_pointer:#"As long as left has not crossed right, keep searching.
            middle_pointer = (left_pointer + right_pointer) // 2  #This finds the middle position.
            if nums[middle_pointer] == target: #"Is the number at the middle position equal to our target?"
                first = middle_pointer
                right_pointer = middle_pointer - 1

            elif nums[middle_pointer] < target:
                left_pointer = middle_pointer + 1

            else:
                right_pointer = middle_pointer - 1
        # Find the last position
        left_pointer = 0
        right_pointer = len(nums) -1
        last = -1

        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if nums[middle_pointer] == target:
                last = middle_pointer
                left_pointer = middle_pointer + 1

            elif nums[middle_pointer] < target:
                left_pointer = middle_pointer + 1
                
            else:
                right_pointer = middle_pointer - 1
        return[first , last]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))




