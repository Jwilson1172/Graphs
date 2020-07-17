from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# add the transversal method
def get_traversal(room_graph, player):

    traversal_path = []

    previous_directions = []
    opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    room_queue = {}
    explored = set()

    while len(explored) < len(room_graph):

        current_room = player.current_room.id
        # print out the current room
        print(current_room)

        if current_room not in explored:
            # if the room is not visited then we have to set it as seen
            # and get the exits for the room
            explored.add(current_room)
            room_queue[current_room] = player.current_room.get_exits()

        elif len(room_queue[current_room]) == 0:
            # if there are no exits then we want toi back track to get to an exit
            prev_dir = previous_directions.pop()
            traversal_path.append(prev_dir)
            player.travel(prev_dir)
        else:
            # finally if the room has already been seen we want to back track
            # to get to un explored areas
            next_dir = room_queue[current_room].pop()
            traversal_path.append(next_dir)
            previous_directions.append(opposite_directions[next_dir])
            player.travel(next_dir)
    return traversal_path


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = get_traversal(room_graph, player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")
