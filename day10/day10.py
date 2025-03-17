"""
Scanning the area, you discover that the entire field you're standing on is
densely packed with pipes; it was hard to tell at first because they're the
same metallic silver color as the "ground". You make a quick sketch of all of
the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but
your sketch doesn't show what shape the pipe has. Based on the acoustics of the
animal's scurrying, you're confident the pipe that contains the animal is one
large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....

If the animal had entered this loop in the northwest corner, the sketch would
instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....

In the above diagram, the S tile is still a 90-degree F bend: you can tell
because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop!
This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF

In the above diagram, you can still figure out which pipes form the main loop:
they're the ones connected to S, pipes those pipes connect to, pipes those
pipes connect to, and so on. Every pipe in the main loop connects to its two
neighbors (including S, which will have exactly two pipes connecting to it, and
which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

Here's the same example sketch with the extra, non-main-loop pipe tiles also
shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ

If you want to get out ahead of the animal, you should find the tile in the
loop that is farthest from the starting position. Because the animal is in the
pipe, it doesn't make sense to measure this by direct distance. Instead, you
need to find the tile that would take the longest number of steps along the
loop to reach from the starting point - regardless of which way around the loop
the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....

You can count the distance each tile in the loop is from the starting point
like this:

.....
.012.
.1.3.
.234.
.....

In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...

Find the single giant loop starting at S. How many steps along the loop does it
take to get from the starting position to the point farthest from the starting
position?
"""


def find_start(pipes):
    for i in range(0, len(pipes)):
        for j in range(0, len(pipes[i])):
            if pipes[i][j] == "S":
                return (i, j)


def find_next_pipe(pipes, i, j, direction):
    """






    . is ground; there is no pipe in this tile.
    S is the starting position
    """
    current = pipes[i][j]

    if current == "S":
        # at the start
        # go to next available pipe

        # check north
        if i > 0:
            if pipes[i - 1][j] in ["|", "7", "F"]:
                i = i - 1
                j = j
                direction = "north"

                return (i, j, direction)

        # check east
        if j + 1 < len(pipes[i][j]):
            if pipes[i][j + 1] in ["-", "7", "J"]:
                i = i
                j = j + 1
                direction = "east"

                return (i, j, direction)

        # check south
        if i + 1 < len(pipes[i]):
            if pipes[i + 1][j] in ["|", "L", "J"]:
                i = i + 1
                j = j
                direction = "south"

                return (i, j, direction)

        # check west (should be redundant)
        if j > 0:
            if pipes[i][j - 1] in ["-", "7", "J"]:
                i = i
                j = j - 1
                direction = "west"

                return (i, j, direction)

    elif current == "|":
        # | is a vertical pipe connecting north and south.
        if direction == "north":
            return (i - 1, j, "north")
        elif direction == "south":
            return (i + 1, j, "south")

    elif current == "-":
        # - is a horizontal pipe connecting east and west.
        if direction == "east":
            return (i, j + 1, "east")
        elif direction == "west":
            return (i, j - 1, "west")

    elif current == "L":
        # L is a 90-degree bend connecting north and east.
        if direction == "south":
            return (i, j + 1, "east")
        elif direction == "west":
            return (i - 1, j, "north")

    elif current == "J":
        # J is a 90-degree bend connecting north and west.
        if direction == "south":
            return (i, j - 1, "west")
        elif direction == "east":
            return (i - 1, j, "north")

    elif current == "7":
        # 7 is a 90-degree bend connecting south and west.
        if direction == "east":
            return (i + 1, j, "south")
        elif direction == "north":
            return (i, j - 1, "west")

    elif current == "F":
        # F is a 90-degree bend connecting south and east.
        if direction == "north":
            return (i, j + 1, "east")
        elif direction == "west":
            return (i + 1, j, "south")

    print(f"Couldn't find next pipe (at {i}, {j}, {direction} [{current}])")
    return None  # shouldn't make it here


# pipes is the 2d list of lists
pipes = list()

with open("input.txt") as fh:
    for line in fh:
        line = line.rstrip()

        pipes.append(list(line))

# starting from the S, walk along the pipe until we loop
# and find the S again, counting our steps
steps = 0

current = None
direction = None
(i, j) = find_start(pipes)

while current != "S":
    (i, j, direction) = find_next_pipe(pipes, i, j, direction)
    steps += 1
    current = pipes[i][j]

print(steps / 2)  # 7030
