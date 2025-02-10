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
    "one": "on1e",
    "two": "tw2o",
    "three": "thr3ee",
    "four": "fou4r",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "sev7en",
    "eight": "ei8ght",
    "nine": "ni9ne"
}

# for each line in the input
with open("input.txt") as fh:
    for line in fh:
        line = line.rstrip()

        first_num = None
        last_num = None

        # replace string numbers with ints
        for text in text_int_dict.keys():
            line = line.replace(text, text_int_dict[text])

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
        sum += int(first_num + last_num)

print(sum)  # 54649
