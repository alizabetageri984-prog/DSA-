numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3
current_sum = sum(numbers[0:window_size])
max_sum = current_sum

for i in range(len(numbers) - window_size + 1):
    current_sum = current_sum - numbers[i-1] + numbers[i + window_size - 1]
    if current_sum > max_sum:
        max_sum = current_sum 
print(max_sum)
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 2

current_sum = sum(numbers[0:window_size])
max_sum = current_sum
for i in range(len(numbers)- window_size + 1):
    current_sum = current_sum - numbers[ i -1] + numbers[i + window_size - 1]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 4

current_sum = sum(numbers[0: window_size])
max_sum = current_sum 
for i in range(len(numbers) - window_size + 1):
    current_sum = current_sum - numbers[i - 1] + numbers[i + window_size - 1]
    if current_sum > max_sum:
        max_sum = current_sum 
print(max_sum)


numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 5
current_sum = sum(numbers[0 : window_size])
max_sum = current_sum

for i in range(len(numbers) - window_size + 1):
    current_sum = current_sum - numbers[ i - 1] + numbers[i + window_size - 1]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8]
window_size  = 2

current_sum = sum(numbers[0 : window_size])
max_sum = current_sum

for i in range(1, len(numbers) - window_size +1):
    current_sum = current_sum - numbers[i - 1] + numbers[i + window_size - 1]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)

#variable_length window_size
def smallest_window(numbers, target):
    left_pointer = 0 
    current_sum = 0
    min_length = float('inf')

    for right_pointer in range (len(numbers)):
        current_sum += numbers[right_pointer]  #growing

        while current_sum >= target: #shrinking
            window_length = right_pointer - left_pointer + 1
            if window_length < min_length:
                min_length = window_length
            current_sum -= numbers[left_pointer]
            left_pointer += 1
    return min_length 
print(smallest_window([1, 2, 3, 4, 5], 11))

def smallest_window(numbers, target):
    left_pointer = 0 
    current_sum = 0
    min_length = float('inf')

    for right_pointer in range(len(numbers)):
        current_sum += numbers[right_pointer]  #growing

        while current_sum >= target:
            window_length = right_pointer - left_pointer + 1
            if window_length < min_length:
                min_length = window_length
            current_sum -= numbers[left_pointer]
            left_pointer += 1
    return min_length 
print(smallest_window([1, 2, 3, 4, 5], 7))
