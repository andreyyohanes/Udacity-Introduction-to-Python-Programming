## Please use this space to test and run your code

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
index = 0
odd_list = []

while len(odd_list) < 5 and index < len(num_list):
    if num_list[index] % 2 != 0:
        odd_list.append(num_list[index])
    index += 1
    
print(sum(odd_list))
