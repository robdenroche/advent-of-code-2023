"""
The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation
of the engine. There are lots of numbers and symbols you don't really
understand, but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum. (Periods (.) do not
count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all
of the part numbers in the engine schematic?
"""


def find_numbers(row):
    # list of (num, start, end) tuples
    number_list = list()

    num = ""
    start = None
    end = None
    j = 0
    while j < len(row):
        if str(row[j]).isnumeric():
            if num == "":   # starting a number
                start = j
            num += str(row[j])
        elif num == "":
            pass
        else:  # done with a number
            end = j - 1
            number_list.append((int(num), start, end))

            num = ""
            start = None
            end = None

        j += 1

    if num != "":
        end = len(row)
        number_list.append((int(num), start, end))

    return number_list


def is_near_symbol(num, start, end, row, array):
    left = max(start - 1, 0)
    right = min(end + 1, len(array[row]) - 1)   # - 1 for zero based index
    top = max(row - 1, 0)
    bottom = min(row + 1, len(array) - 1)   # - 1 for zero based index

    for i in range(top, bottom + 1):    # + 1 to include bottom
        for j in range(left, right + 1):    # + 1 to include right
            # print(i,j)
            if not str(array[i][j]).isnumeric() and str(array[i][j]) != ".":
                # print(num, array[i][j])
                return True
            
    return False


# part number sum
sum = 0

# 2d array of the input
array = list()

with open("input.txt") as fh:
    for line in fh:
        line = line.rstrip()

        array.append(list(line))

for i in range(len(array)):
    for (num, start, end) in find_numbers(array[i]):
        if is_near_symbol(num, start, end, i, array):
            sum += num


print(sum)  # 535235
