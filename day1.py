#"find the largest number in the list."
#Start
#Read the list of numbers
#Assume the first element is the largest
#Compare each remaining element with the current largest
#If an element is greater, update the largest
#Repeat until all elements are checked
#Display the largest number
#Stop

score = [10,20,30, 40, 50, 60,70,80]
largest = score[0]
for num in score:
    if num > largest:
        largest = num
print("The largest number is:", largest)

#Write pseudocode, then code: "Check if a given number exists in the list." (Don't use Python's in keyword — pretend it doesn't exist, loop through manually and compare each element.)
number_to_check = 40
#pseudocode:
#start
#read the lsit of numbers 
#assume the number does not exist in the lsit
#loop through each element in the list
#compare the current element with the number to check 
# if they are equal, set a flag to indicate the number exists and break the loop
#if the loop compltes without finding the number, the flag remains false
#display whether the number exists in the list or not 
exists = False
for num in score:
    if num == number_to_check:
        exists = True
        break
print("The number exists in the list:", exists)
#write pseudocode first, then code: "Count how many even numbers are in the list."

#Hint: a number is even if number % 2 == 0 (the % operator gives you the remainder after division — if dividing by 2 leaves no remainder, it's even)
score = [10,20,30, 40, 50, 60,70,80]
even_count = 0
for num in score:
    if num % 2 == 0:
        even_count += 1
print("The number of even numbers in the list is:", even_count)
#reversing a list manually, without using reversed() or list[::-1].
#pseudocode:
#start
#read the list of numbers
#intialize an empty list to hold the reversed numbers 
#loop through theoriginal list from the last index to the frist index 
#append each element to the new list 
#display the reversed list 
reversed_score = []
for i in range(len(score) - 1, -1, -1):
    reversed_score.append(score[i])
print("The reversed list is:", reversed_score)
#Write pseudocode, then code: "Find the sum of all elements in the list." (Don't use Python's built-in sum() — loop through manually.)
#pseudocode:
#start
#read the list of numbers
#initialize a variable to hold the sum, starting at 0 
#loop through each element int the list
#add the current element to the sum variable
#siplay the final sum 
total_sum = 0
for num in score:
    total_sum += num
print("the sum of all elements in the list is:", total_sum)
#"Find the second largest number in the list."
#1. Start
#2. Assume the first element is both largest and second_largest initially
#3. Loop through each remaining element
#4. If the current element is bigger than largest:
       #second_largest becomes the old largest
       #largest becomes the current element
#5. Else if the current element is bigger than second_largest (but not bigger than largest):
      # update second_largest
#6. Display second_largest
#7. stop
second_largest = score[0]
largest = score[0]
for num in score:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("the second largest number in the lsit is:", second_largest)
#"Remove all duplicate values from a list, keeping only unique values." Don't use set()
#1. Start
#2. Create a new, empty list to hold unique values
#3. Loop through each element in the original list
#4. For each element, check: is it ALREADY in the new list?
#5. If NOT already there → add it to the new list
#6. If it IS already there → skip it
#7. Display the new list
unique_values = []
for num in score:
    found = False
    for existing in unique_values:
        if existing == num:
            found = True
            break
    if not found:
        unique_values.append(num)
print("the list with unique values is:", unique_values)
#palindrome check:

#"Check if a list reads the same forward and backward" — like [1, 2, 3, 2, 1].
#1. Start
#2. Set left_pointer = 0
#3. Set right_pointer = len(score) - 1
#4. Repeat while left_pointer is less than right_pointer:
#       a. Compare score[left_pointer] with score[right_pointer]
#       b. If NOT equal → it's NOT a palindrome, stop
#       c. Otherwise → left_pointer += 1, right_pointer -= 1
#5. If loop finished without mismatch → it IS a palindrome
is_palindrome = True
left_pointer = 0
right_pointer = len(score) -1
while left_pointer < right_pointer:
    if score[left_pointer] != score[right_pointer]:
        is_palindrome = False
        break
    left_pointer += 1
    right_pointer -= 1
print("the list is a palindrome:", is_palindrome)
#"Find the smallest and largest number in a single pass" — one loop, tracking both simultaneously
score = [50, 20, 30, 40, 10, 60, 70, 80]
smallest = score[0]
largest = score[0]
for num in score:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("the smallest number is:", smallest)
print("the largest number is:", largest)
#Write pseudocode, then code: "Count how many vowels (a, e, i, o, u) are in a given string." (Treat the string like a list of characters — you can loop through a string exactly like a list.)
string = "Hello, World!"
#pseudocode:
#start
#read the string
#initialize a varaible to hold the count of vowels, starting at 0 
#loop through each character in the string 
#check if the current character is a vowel (a, e, i, o, u)
#if it is a vowel, increment the count vaiable
#dispaly the finalcount of vowels
vowel_count = 0
for char in string:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
print("the number of vowels in the string is:", vowel_count)
#Write pseudocode, then code: "Check if two strings are anagrams of each other" — meaning they contain the exact same letters, just rearranged (e.g., "listen" and "silent"). Think about it: how could you check this using something you already built recently (hint: sorting, or counting each letter)?
string1 = "listen"
string2 = "silent"
#pseudocode:
#start
#read the two strings
#check if the lengths of the two strings are eqaul
#if not equal , they cannot be anagrams, display false and stop
#intialize two empty dictionaries to hold the counts of each letter in both strings 
#loop through each character in the first string, incrementing the count in the first dictionary 
string1_count = {}
for char in string1:
    string1_count[char] = string1_count.get(char, 0) + 1
string2_count = {}
for char in string2:
    string2_count[char] = string2_count.get(char, 0) + 1
#check if the two dictionaries are equal
if string1_count == string2_count:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#(Basic sorting — Bubble Sort, understanding over memorizing) Write pseudocode, then code: "Sort a list of numbers from smallest to largest, WITHOUT using Python's built-in sort() or sorted()."
score = [64, 34, 25, 12, 22, 11, 90]
#pseudocode:
#start
#raed the list if numbers
#loop though the list multiple times, comparing adjacent elements 
#if the current element is greater than the next element, swap them
#repeat until no more swaps are needed(meaning the list is sorted)
n = len(score)
for i in range(n):
    for j in range(0, n-i-1):
        if score[j] > score[j + 1]:
            score[j], score[j + 1] = score[j + 1], score[j]
print("the sorted list is:", score)
