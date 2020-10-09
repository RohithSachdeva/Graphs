from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []


traversed = {}
reverse = []
rooms_todo = []

while len(room_graph) > len(traversed):
    current_room = player.current_room.id
    choices = player.current_room.get_exits()
    rooms_todo.append(current_room)

    if current_room not in traversed:
        traversed[current_room] = choices

    if len(traversed[current_room]) > 0:
        x = traversed[current_room].pop()
        traversal_path.append(x)
        reverse.append #append these direction but inverted 

        """
        how can invert the cardinal directions?  .. so a dictionary where n = s ... or create a function but not sure how to utilize it .. anyways figure it out tomorrw 

        have player.travel(x)

        else: 
            pop the newly reverse array and append it to traversal path and have player travel that and that should travel all the rooms.. well see if its under 2000 moves
        """













# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")



