from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

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
reverseCardinal = {"n":"s", "s":"n", "e":"w", "w":"e"}

while len(room_graph) > len(traversed):
    #While there are rooms unexplored
    current_room = player.current_room.id #Get current room
    choices = player.current_room.get_exits() #See possible edges of node 

    if current_room not in traversed:
        traversed[current_room] = choices #If it hasn't been explored, view its cardinal choices/exits.
    
    if len(traversed[current_room]) > 0:
        #While there are unexplored exits in your current room
        x = traversed[current_room].pop()
        #Pop the room into the stack of the traversed array; we will check this room while there are previous rooms in the stack.  This stack of rooms is kept in a separate array than the main path.  
        traversal_path.append(x)
        #Append the popped object to the main traversal path list
        reverse.append(reverseCardinal[x])
        #Append the reversed direction to a separate list that will execute if you reach a dead end 
        player.travel(x)
        #Travel to the popped room
    else:
        #When there are no rooms to be explored; start back tracking with inverted directions
        rev = reverse.pop()
        traversal_path.append(rev) #Append this to your main path to leave the deadend room
        player.travel(rev) #Travel in reverse

    




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
