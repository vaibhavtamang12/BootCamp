# Type Casting
# Question 1 -  Write a Python program that takes a string input and returns its integer equivalent.
n = input()
i = int(n)
print(i)

# Question 2 -  Write a Python program that takes a float input and returns its string equivalent with two decimal places. For example, if the input is 3.14159, the output should be "3.14"
number = float(input())
print("{:.2f}".format(number))

# Question 3 - Write a Python program that takes a list of strings and returns a list of integers.
l = list(map(str, input().split()))
new_list = []
for i in range(len(l)):
    n = int(l[i])
    new_list.append(n)
print(new_list)

