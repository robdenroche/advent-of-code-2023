"""
There's just one problem - many of the springs have fallen into disrepair, so
they're not actually sure which springs would even be safe to use! Worse yet,
their condition records of which springs are damaged (your puzzle input) are
also damaged! You'll need to help them repair the damaged records.

In the giant field just outside, the springs are arranged into rows. For each
row, the condition records show every spring and whether it is operational (.)
or damaged (#). This is the part of the condition records that is itself
damaged; for some springs, it is simply unknown (?) whether the spring is
operational or damaged.

However, the engineer that produced the condition records also duplicated some
of this information in a different format! After the list of springs for a
given row, the size of each contiguous group of damaged springs is listed in
the order those groups appear in the row. This list always accounts for every
damaged spring, and each number is the entire size of its contiguous group
(that is, groups are always separated by at least one operational spring: ####
would always be 4, never 2,2).

So, condition records with no unknown spring conditions might look like this:

#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
However, the condition records are partially damaged; some of the springs'
conditions are actually unknown (?). For example:

???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
Equipped with this information, it is your job to figure out how many different
arrangements of operational and broken springs fit the given criteria in each
row.

In the first line (???.### 1,1,3), there is exactly one way separate groups of
one, one, and three broken springs (in that order) can appear in that row: the
first three unknown springs must be broken, then operational, then broken
(#.#), making the whole row #.#.###.

The second line is more interesting: .??..??...?##. 1,1,3 could be a total of
four different arrangements. The last ? must always be broken (to satisfy the
final contiguous group of three broken springs), and each ?? must hide exactly
one of the two broken springs. (Neither ?? could be both broken springs or they
would form a single contiguous group of two; if that were true, the numbers
afterward would have been 2,3 instead.) Since each ?? can either be #. or .#,
there are four possible arrangements of springs.

The last line is actually consistent with ten different arrangements! Because
the first number is 3, the first and second ? must both be . (if either were #,
the first number would have to be 4 or higher). However, the remaining run of
unknown spring conditions have many different ways they could hold groups of
two and one broken springs:

?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
In this example, the number of possible arrangements for each row is:

???.### 1,1,3 - 1 arrangement
.??..??...?##. 1,1,3 - 4 arrangements
?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
????.#...#... 4,1,1 - 1 arrangement
????.######..#####. 1,6,5 - 4 arrangements
?###???????? 3,2,1 - 10 arrangements
Adding all of the possible arrangement counts together produces a total of 21
arrangements.

For each row, count all of the different arrangements of operational and broken
springs that meet the given criteria. What is the sum of those counts?

"""


def check_arrangement(spring, count) -> bool:
    assert "?" not in spring

    c_pos = 0
    group_len = 0
    for i in range(0, len(spring)):
        if spring[i] == "#":
            group_len += 1
        elif spring[i] == "." and group_len > 0:
            if group_len != int(count[c_pos]):
                return False
            c_pos += 1
            group_len = 0

    if group_len > 0:
        if group_len != int(count[c_pos]):
            return False
        c_pos += 1

    if c_pos != len(count):
        return False

    return True


def permute_arrangements(spring) -> list():
    arrangements = list()

    # collect ? positions
    unknowns = list()
    for i in range(0, len(springs)):
        if springs[i] == "?":
            unknowns.append(i)

    for i in range(0, len(unknowns)):
        new_spring = spring

    return arrangements


springs = list()
counts = list()

with open("sample.txt") as fh:
    for line in fh:
        line = line.rstrip()

        (spring, count) = line.split(" ")

        springs.append(list(spring))
        counts.append(count.split(","))

# running count of possible arrangements
sum = 0

for i in range(0, len(springs)):

    # generate all possible ? configurations and count how many pass
    for spring in permute_arrangements(springs[i]):
        if check_arrangement(spring, counts[i]) is True:
            sum += 1

print(sum)  #
