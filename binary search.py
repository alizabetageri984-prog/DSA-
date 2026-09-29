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
#There is an integer array nums sorted in ascending order (with distinct values).

##Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
class Solution(object):
    def search(self, nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if nums[middle_pointer] == target:
                return middle_pointer

                #check weather the left half after roatation is sorted?
            if nums[left_pointer] <= nums[middle_pointer]:
                #check wheater to the target is right or left 
                #to check left 

                if nums[left_pointer] <= target < nums[middle_pointer]:
                    right_pointer = middle_pointer - 1

                else:
                    left_pointer = middle_pointer + 1

            else: # this runs when if condition that the left part is sorted is not true 
                    # this checks that is target is in right sorted part and decide to move left or right 
                if nums[middle_pointer] < target <= nums[right_pointer]:
                    left_pointer = middle_pointer + 1
                else:
                    right_pointer = middle_pointer - 1
        return - 1
print(Solution().search([4,5,6,7,0,1,2],0))

#There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

#Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

#Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

#You must decrease the overall operation steps as much as possible.
class Solution(object):
    def search(self, nums, target):
        left_pointer = 0
        right_pointer = len (nums) -1

        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) // 2

            if nums[middle_pointer] == target:
                return True

            if nums[left_pointer] == nums[middle_pointer] == nums[right_pointer]:
                left_pointer += 1
                right_pointer -= 1
                continue
            if nums[left_pointer] <= nums[middle_pointer]:

                if nums[left_pointer] <= target < nums[middle_pointer]:
                    right_pointer -= 1

                else:
                    left_pointer += 1
            else:
                if nums[middle_pointer] < target <= nums[right_pointer]:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return False
print(Solution().search([2,5,6,0,0,1,2],0))


#Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
#Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
class Solution(object):
    def findMin(self, nums):

        left_pointer = 0
        right_pointer = len(nums)-1

        while left_pointer < right_pointer:#"Keep repeating the loop as long as left and right are pointing to different positions."
            middle_pointer = (left_pointer+right_pointer)//2

            if nums[middle_pointer] > nums[right_pointer]:#"The middle value is bigger than the right value, so the minimum is on the right side of mid. Throw away the left side, including mid."
                left_pointer = middle_pointer + 1

            elif nums[middle_pointer] < nums[right_pointer]:#"The minimum is at mid or somewhere to its left, so move right to mid but keep mid."
                right_pointer = middle_pointer

            else:
                right_pointer = right_pointer - 1 #"The middle and right values are equal, so the right value gives us no useful information. Remove that one duplicate and continue searching."
        return nums[left_pointer]
print(Solution().findMin([1,3,5]))
print(Solution().findMin([2,2,2,0,1]))

#Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

#Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

#Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

#Return the minimum integer k such that she can eat all the bananas within h hours.
class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1 #The slowest possible speed is 1 banana per hour.
        right = max(piles)# max(piles) finds the biggest pile.

        while left <= right:#"Keep searching while there are still possible speeds to check."
            k = (left + right) //2#"Can Koko finish all the bananas if she eats 6 bananas per hour?"

            hours = 0

            for pile in piles: #This goes through each pile one by one.
                hours += (pile + k - 1) // k #How many hours are needed to finish the current pile

            if hours <= h: #"Can Koko finish within the available 8 hours?"
                right = k -1#Since k = 6 works, maybe Koko can eat even slower
            else:
                left = k + 1
        return left #At the end of Binary Search, left becomes the smallest speed that works.
print(Solution().minEatingSpeed([3,6,7,11], 8))


