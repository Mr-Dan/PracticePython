
str = "косинус"

# 1
for i in range(len(str)):
    print(str[0:len(str)-i])
print()

# 2
for i in range(len(str)):
    print(" "*i, str[i:])
print()

# 3
for i in range(len(str)+1):
    print(str[:i])
print()

# 4
for i in range(len(str)+1):
    print(" "*(len(str)-i), str[len(str)-i:])
print()