import math, sys

file_name = sys.argv[1]

def Check(n: int) -> bool:
    for x in range(2, int(math.sqrt(n))):
        if n % x == 0:
            return False
    else:
        return True

with open(file_name) as input_numbers:
    for line in input_numbers:
        number = int(line)
        print(1 if Check(number) else 0)