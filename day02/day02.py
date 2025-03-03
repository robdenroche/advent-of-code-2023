"""
As you walk, the Elf shows you a small bag and some cubes which are either red,
 green, or blue. Each time you play this game, he will hide a secret number of
 cubes of each color in the bag, and your goal is to figure out information
 about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach
into the bag, grab a handful of random cubes, show them to you, and then put
them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle
input). Each game is listed with its ID number (like the 11 in Game 11: ...)
followed by a semicolon-separated list of subsets of cubes that were revealed
from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back
again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red
cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the
bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag
had been loaded with that configuration. However, game 3 would have been
impossible because at one point the Elf showed you 20 red cubes at once;
similarly, game 4 would also have been impossible because the Elf showed you
15 blue cubes at once. If you add up the IDs of the games that would have been
possible, you get 8.

Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the
IDs of those games?
"""


# running sum of passing game IDs
sum = 0

# total number of cubes defining a good game
total_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_game_id(line):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_id = line.split(":")[0].split(" ")[1]

    return int(game_id)


def get_max_dict(line):
    max_dict = dict()

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    games = line.split(": ")[1].split("; ")

    for game in games:
        colour_counts = game.split(", ")
        for colour_count in colour_counts:
            [count, colour] = colour_count.split(" ")

            if colour in max_dict:
                max_dict[colour] = max(max_dict[colour], int(count))
            else:
                max_dict[colour] = int(count)

    return max_dict


def good_game(max_dict, total_dict):
    for colour in total_dict.keys():
        if colour in max_dict and max_dict[colour] > total_dict[colour]:
            return False
   
    return True


# for each line in the input
with open("input.txt") as fh:
    for line in fh:
        line = line.rstrip()

        game_id = get_game_id(line)

        max_dict = get_max_dict(line)

        if good_game(max_dict, total_dict):
            sum += game_id

print(sum)  # 3099


"""
As you continue your walk, the Elf poses a second question: in each game you
played, what is the fewest number of cubes of each color that could have been
in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, the game could have been played with as few as 4 red, 2 green, and
6 blue cubes. If any color had even one fewer cube, the game would have been
impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue
cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue
cubes multiplied together. The power of the minimum set of cubes in game 1 is
48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these
five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What
is the sum of the power of these sets?
"""

# running sum of power of minimum cube sets
sum = 0


def min_set_power(max_dict):
    power = 1
    for colour in max_dict.keys():
        power *= max_dict[colour]

    return power


# for each line in the input
with open("input.txt") as fh:
    for line in fh:
        line = line.rstrip()

        game_id = get_game_id(line)

        max_dict = get_max_dict(line)

        sum += min_set_power(max_dict)

print(sum)  # 72970
