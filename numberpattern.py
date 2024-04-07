# Increasing Numbers Triangle
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()

# Decreasing Numbers Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()


# Left-aligned Increasing Numbers Triangle
n = 5
for i in range(1, n+1):
    spaces = ' ' * (n-i)
    print(spaces, end='')
    for j in range(1, i+1):
        print(j, end='')
    print()

# Left-aligned Decreasing Numbers Triangle
n = 5
for i in range(n, 0, -1):
    spaces = ' ' * (n-i)
    print(spaces, end='')
    for j in range(1, i+1):
        print(j, end='')
    print()

# Left-aligned Decreasing Numbers Triangle (Reversed)
n = 5
for i in range(1, n+1):
    spaces = ' ' * (n-i)
    print(spaces, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()

# ight-aligned Decreasing Numbers Triangle
n = 5
for i in range(n+1):
    spaces = ' ' * i
    print(spaces, end='')
    for j in range(n-i, 0,-1):
        print(j, end='')
    print()

# Right-aligned Decreasing Numbers Triangle (Grouped)
n = 5
for i in range(n, 0, -1):
    spaces = ' ' * i
    for j in range(n-i+1, n+1):
        print(spaces, end='')
        print(str(j) * (n-i) * 2 + str(j))
        break

# Right-aligned Decreasing Numbers Triangle (Grouped, Reversed)
n = 5
for i in range(n+1):
    spaces = ' ' * i
    for j in range(n-i+1, n+1):
        print(spaces, end='')
        print(str(j) * (n-i) * 2 + str(j))
        break


