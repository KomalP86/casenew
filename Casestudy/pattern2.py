def print_pattern(name):
    length = len(name)
    for i in range(1, length + 1):
        print(name[:i])

name = "SANDEEP"
print_pattern(name)
