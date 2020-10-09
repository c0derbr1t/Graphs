from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque

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

# create a traversal graph that is initialized with the starting room
traversal_graph = {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}

# naive solution
while len(traversal_graph) < 500:
    print("length:")
    print(len(traversal_graph))
    current_room = player.current_room.id
    current_exits = player.current_room.get_exits()
    rand_direction = random.choice(current_exits)

    if rand_direction == "n":
        opposite_direction = "s"
    elif rand_direction == "s":
        opposite_direction = "n"
    elif rand_direction == "e":
        opposite_direction = "w"
    elif rand_direction == "w":
        opposite_direction = "e"

    traversal_path.append(rand_direction)
    player.travel(rand_direction)

    new_room = player.current_room.id
    new_exits = player.current_room.get_exits()

    if current_room in traversal_graph:
        traversal_graph[current_room][rand_direction] = new_room

    else:
        for item in current_exits:
            traversal_graph[current_room][item] = '?'

        traversal_graph[current_room][rand_direction] = new_room

    if new_room in traversal_graph:
        traversal_graph[new_room][opposite_direction] = current_room

    else:
        update = {}
        for new_item in new_exits:
            update[new_item] = '?'

        traversal_graph[new_room] = update
        traversal_graph[new_room][opposite_direction] = current_room


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
