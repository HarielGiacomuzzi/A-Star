#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys
import Queue
from common import *

# ==========================================
# PathFinder A Star
# ==========================================

class PathFinder_A_Star:

    def __init__(self):
        # TODO initialize your attributtes here if needed
        pass

    # ------------------------------------------
    # Cost
    # ------------------------------------------

    def get_cost(self, x1, y1, x2, y2):
        # TODO Cost of movement from (x1, y1) to (x2, y2)
        return 0

    # ------------------------------------------
    # Heuristic
    # ------------------------------------------

    def heuristic(self, x1, y1, x2, y2):
       # TODO heuristic function returns an integer
       return 0
    
    # ------------------------------------------
    # Solve
    # ------------------------------------------

    def solve(self, sx, sy, gx, gy, map, map_width, map_height):
        # TODO return a list of movements (may be empty) if plan found, otherwise return None
        return None

    # ------------------------------------------
    # Get solvable
    # ------------------------------------------

    def get_solvable(self):
        # TODO return True if plan found, otherwise False
        return False

    # ------------------------------------------
    # Get max tree height
    # ------------------------------------------

    def get_max_tree_height(self):
        # TODO return max tree height if plan found, otherwise None
        return None

    # ------------------------------------------
    # Get min moves
    # ------------------------------------------

    def get_min_moves(self):
        # TODO return size of minimal plan to reach goal if plan found, otherwise None
        return None

# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 2:
        map_name = sys.argv[1]
    else:
        map_name = DEFAULT_MAP
    print "Loading map: " + map_name
    sx, sy, gx, gy, map, map_width, map_height = read_map(map_name)
    plan = PathFinder_A_Star().solve(sx, sy, gx, gy, map, map_width, map_height)
    if plan == None:
        print "No plan was found"
    else:
        print "Plan found:"
        for i, move in enumerate(plan):
            if move == MOVE_UP:
                print i, ": Move Up"
            elif move == MOVE_DOWN:
                print i, ": Move Down"
            elif move == MOVE_LEFT:
                print i, ": Move Left"
            elif move == MOVE_RIGHT:
                print i, ": Move Right"
            else:
                print i, ": Movement unknown = ", move