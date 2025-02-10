"""
The newly-improved calibration document consists of lines of text; each line 
originally contained a specific calibration value that the Elves now need to 
recover.  On each line, the calibration value can be found by combining the 
first digit and the last digit (in that order) to form a single two-digit 
number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, 
and 77.  Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the 
calibration values?
"""

# running sum
sum = 0

# for each line in the input
with open("input.txt") as fh:
    for line in fh:
        line = line.rstrip()

        first_num = None
        last_num = None

        # get list of ints from line
        for i in line:
            if i.isnumeric():
                if first_num is None:
                    first_num = i
                last_num = i
        
        # confirm we found numbers and sum
        assert first_num is not None
        assert last_num is not None
        sum += int(first_num + last_num)

print(sum)  # 54081


"""
Your calculation isn't quite right. It looks like some of the digits are 
actually spelled out with letters: one, two, three, four, five, six, seven, 
eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and 
last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.
"""

# running sum
sum = 0

# text to int
text_int_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


# find and replace the leftmost text number with its int
def replace_leftmost_number(line):
    leftmost_pos = None
    leftmost_text = None

    for text in text_int_dict.keys():
        index = line.find(text)
        if index > -1:
            if leftmost_pos is None or index < leftmost_pos:
                leftmost_pos = index
                leftmost_text = text

    if leftmost_text is not None:
        line = line.replace(leftmost_text, text_int_dict[leftmost_text])
    return line
    

# for each line in the input
with open("input.txt") as fh:
    for line in fh:
        line = line.rstrip()

        first_num = None
        last_num = None

        print(line)
        # replace leftmost number until no changes are made
        old_line = None
        new_line = line
        while old_line != new_line:
            old_line = new_line
            new_line = replace_leftmost_number(old_line)
        line = new_line

        print(line)

        # convert text numbers to ints
        for text in text_int_dict.keys():
            line = line.replace(text, text_int_dict[text])

        # get list of ints from line
        for i in line:
            if i.isnumeric():
                if first_num is None:
                    first_num = i
                last_num = i

        # confirm we found numbers and sum
        assert first_num is not None
        assert last_num is not None
        print(first_num + last_num)
        print()

        sum += int(first_num + last_num)

print(sum)  # 54627
