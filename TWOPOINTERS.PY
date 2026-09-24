#ou are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.

def water_contains(height):
    left_pointer = 0
    right_pointer = len(height)-1
    max_water = 0
    while left_pointer < right_pointer:
        current =min(height[left_pointer], height[right_pointer ]) * (right_pointer - left_pointer)

        if height[left_pointer]  < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -=1

        if max_water < current:
            max_water = current
    return max_water
print(water_contains(height = [1,8,6,2,5,4,8,3,7]))

#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Sort
 #↓
#Pick i
 #↓
#left = i + 1
#right = last
# ↓
#Add 3 numbers
# ↓
#0? → Save
#< 0? → left++
##> 0? → right--
# ↓
#Return result
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left_pointer = i + 1
            right_pointer = len(nums)-1 

            while left_pointer < right_pointer:
                total = nums[i] + nums[left_pointer] + nums[right_pointer]

                if total == 0:
                    result.append([nums[i] , nums[left_pointer] , nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1

                    # Skip duplicate values after finding a triplet.
                    while (left_pointer < right_pointer and
                           nums[left_pointer] == nums[left_pointer - 1]):
                        left_pointer += 1
                    while (left_pointer < right_pointer and
                           nums[right_pointer] == nums[right_pointer + 1]):
                        right_pointer -= 1

                elif total < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return result
print(Solution().threeSum([-1,0,1,2,-1,-4]))
#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#0 <= a, b, c, d < n
#a, b, c, and d are distinct.
#nums[a] + nums[b] + nums[c] + nums[d] == target
#You may return the answer in any order.
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:

                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        # Skip duplicate third numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate fourth numbers
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result
#Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

#0 <= i, j, k, l < n
#nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:

                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        # Skip duplicate third numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate fourth numbers
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result
print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
#Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

#In one move, you can increment n - 1 elements of the array by 1.
class Solution(object):
    def minMoves(self, nums):
        smallest = min(nums)

        moves = 0

        for num in nums:
            moves = moves + (num - smallest)

        return moves

#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
class Solution(object):
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
        k = m + n - 1

        while  j >= 0:
            if i >= 0 and  nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        return nums1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

solution = Solution()

print(solution.merge(nums1, m, nums2, n))
#"The time complexity is O(m + n), because we traverse the elements of both arrays at most once. The space complexity is O(1), because we merge in-place without using extra space."




#Given a sorted integer array nums, remove duplicates in-place such that each unique element appears only once. Return the count of unique elements k. The first k elements of nums must hold the unique values.
class Solution(object):
    def removeDuplicates(self, nums):
        slow_pointer = 0
        for fast_pointer in range(1 , len(nums)):
            if nums[slow_pointer] != nums[fast_pointer]:
                slow_pointer += 1
                nums [ slow_pointer] = nums[fast_pointer]
        return  slow_pointer + 1
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order
class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0]*n#creating empty list to store the new values result = [0, 0, 0, 0, 0]

        left_pointer = 0
        right_pointer = n - 1

        for position in range(n - 1, -1, -1):#start , stop, step
            if abs(nums[left_pointer]) > abs (nums[right_pointer]):
                result[position] = nums[left_pointer] **2
                left_pointer += 1

            else:
                result[position] = nums[right_pointer] ** 2
                right_pointer -= 1

           
        return result
solution = Solution()

print(solution.sortedSquares([-4, -1, 0, 3, 10]))
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
class Solution(object):
    def trap(self, height):
        left_pointer = 0               #set a pointers
        right_pointer = len(height) - 1
        left_max = 0#height of the left bar is filhal is 0
        right_max = 0#height of the right bar is filhal is 0
        total_water = 0 

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                if height[left_pointer] >= left_max:
                    left_max = height[left_pointer]
                else:
                    total_water += left_max - height[left_pointer]

                left_pointer += 1

            else:
                if height[right_pointer] >= right_max:
                    right_max = height[right_pointer]

                else:
                    total_water += right_max - height[right_pointer]

                right_pointer -= 1

        return total_water

height = [4, 2, 0, 3, 2, 5]

print(Solution().trap(height))


#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0

        while i < len(word1) or i < len(word2):

            if i < len(word1):
                result += word1[i]

            if i < len(word2):
                result += word2[i]

            i += 1

        return result


print(Solution().mergeAlternately("abc", "pqr"))

#Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

#In one move, you can increment or decrement an element of the array by 1
class Solution(object):
    def minMoves2(self, nums):
        nums.sort()

        median = nums[len(nums) // 2]

        moves = 0

        for num in nums:
            moves += abs(num - median)

        return moves

    #You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        
        left_pointer = 0
        right_pointer = len(people)-1

        Boats = 0

        while left_pointer <= right_pointer:

            if people[left_pointer] + people [right_pointer] <= limit:
                left_pointer += 1 # moves if are in limit 

            right_pointer -= 1 # moves if they are not in limit 

            Boats += 1
        return Boats
print(Solution().numRescueBoats([3,2,2,1],3))
#You are given an integer array nums and an integer k.

#In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

#Return the maximum number of operations you can perform on the array.
class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()

        left_pointer = 0
        right_pointer = len(nums) - 1

        maximum = 0

        while left_pointer < right_pointer:
            total = nums[left_pointer] + nums[right_pointer] 
            if total == k:
                maximum += 1

                left_pointer += 1
                right_pointer -=1

            elif total < k:
                left_pointer += 1

            else:
                right_pointer -= 1

        return maximum
print(Solution().maxOperations([1,2,3,4],5))

#Given a string s, return the longest palindromic substring in s.
class Solution(object):
    def longestPalindrome(self, s):
        longest = ""

        for i in range(len(s)):
            left = i
            right = i

            # Odd length
            while left >= 0 and right < len(s) and s[left] == s[right]:

                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]

                left -= 1
                right += 1

            # Even length
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]

                left -= 1
                right += 1

        return longest
print(Solution().longestPalindrome("babad"))
            
