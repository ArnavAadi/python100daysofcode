# num = int(input("enter a no: "))

# for number in range(1, num):
#     if num % number == 0:
#         print(number)

# sent = input("enter a sentence \n")
# sent_list = []

# for let in sent:
#     sent_list.append(let)

# new_sent = ""

# for num in range(len(sent)-1, -1, -1):
#     new_sent += sent_list[num]

# print(new_sent)


# A Python program to print all
# permutations using library function
# from itertools import permutations

# # # Get all permutations of [1, 2, 3]
# # perm = permutations([1, 2, 3])

# # # Print the obtained permutations
# # for i in list(perm):
# #     print(i)


x = 0
y = 1


def number():
    global x
    global y
    add = x+y
    x = y
    y = add
    return y


num = int(input("enter a no"))
nums = []

while y < num:
    nums.append(number())

differ_a = nums[-1] - num
differ_b = num - nums[-2]

if differ_a > differ_b:
    print(nums[-2])
else:
    print(nums[-1])
