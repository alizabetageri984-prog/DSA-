

    #Number Hashing using list 
n = [5, 3, 3, 2, 2, 1, 5, 5, 7, 5, 10]

hash_list = [0] * 11

print("Hash list:", hash_list)
print("Hash list length:", len(hash_list))
print("Maximum number:", max(n))

for x in n:
    print("Processing:", x)
    hash_list[x] += 1

print("Final frequency:", hash_list)

m = [10, 111, 1, 9, 5, 67, 2]

for x in m:
    if x < 1 or x > 10:
        print(0)
    else:
        print(hash_list[x])

#character hashing 

s = "azyxyzaaa"
q = ["a", "a", "y", "x"]

hash_list = [0] * 26

# Precompute frequencies
for ch in s:
    index = ord(ch) - 97
    hash_list[index] += 1

# Answer queries
for ch in q:
    index = ord(ch) - 97
    print(hash_list[index])
#Number Hashing using Dictionary

n = [5, 3, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

hash_map = {}

# Precompute frequencies
for x in n:
    if x in hash_map:
        hash_map[x] += 1
    else:
        hash_map[x] = 1

# Answer queries
for x in m:
    print(hash_map.get(x, 0))

#. Character Hashing using Dictionary

s = "azyxyzaaa"
q = ["a", "a", "y", "x"]

hash_map = {}

# Precompute frequencies
for ch in s:
    if ch in hash_map:
        hash_map[ch] += 1
    else:
        hash_map[ch] = 1

# Answer queries
for ch in q:
    print(hash_map.get(ch, 0))
