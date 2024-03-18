def print_pattern(name):
    length = len(name)
    for i in range(length, 0, -1):
        print(name[:i])

name = "SANDEEP"
print_pattern(name)
