# Question 1: https://codeforces.com/problemset/problem/136/A

# Solution:
n = int(input())

p = list(map(int, input().split()))
l = []
for i in range(len(p)):
    l.insert(p[i]-1,i+1)
print(l)


# Question 2: https://codeforces.com/problemset/problem/200/B

# Solution:
n = int(input())

m = list(map(int, input().split()))

percent = 0

for i in range(len(m)):
    percent = percent + (m[i] /100)
total = (percent / n) * 100
print(total)



# Question 3: https://codeforces.com/problemset/problem/228/A

# Solution:
m = list(map(int, input().split()))

s = set(m)

l = len(s)

print(4-l)


# Question 4:  https://codeforces.com/problemset/problem/520/A

# Solution:
n = int(input())

word = input()

count = 0

for i in word:
    for j in word:
        if i == j:
            count = count + 1

if count > 1:
    print("NO")

else:
    print("YES")


# Question 5: https://codeforces.com/problemset/problem/785/A

# Solution:
n = int(input())

face = 0

for i in range(n):
    shape = input()
    if shape == "Tetrahedron":
        face += 4
    elif shape == "Cube":
        face += 6
    elif shape == "Octahedron":
        face += 8
    elif shape == "Dodecahedron":
        face += 12
    else:
        face += 20
print(face)