#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import unittest
from common import *
from pathfinder import *

# Map definitions
TRIVIAL = "trivial.txt"
TRIVIAL_SOLUTION = []
TRIVIAL_MAX_TREE_HEIGHT = 0
TRIVIAL_GRADE = 0.25

EASY = "easy.txt"
EASY_SOLUTION = [
    MOVE_UP, MOVE_UP, MOVE_UP, MOVE_UP, MOVE_UP, MOVE_UP,
    MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT]
EASY_MAX_TREE_HEIGHT = 9
EASY_GRADE = 0.25

MEDIUM = "medium.txt"
MEDIUM_SOLUTION = [
    MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN, MOVE_DOWN,
    MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT,
    MOVE_UP, MOVE_UP, MOVE_UP,
    MOVE_RIGHT, MOVE_RIGHT, MOVE_RIGHT,
    MOVE_UP, MOVE_UP,
    MOVE_LEFT, MOVE_LEFT, MOVE_LEFT,
    MOVE_UP, MOVE_UP,
    MOVE_LEFT, MOVE_LEFT, MOVE_LEFT]
MEDIUM_MAX_TREE_HEIGHT = 28
MEDIUM_GRADE = 0.25

# ==========================================
# Test A*
# ==========================================

class Test_A_Star(unittest.TestCase):

    # ------------------------------------------
    # Setup
    # ------------------------------------------

    @classmethod
    def setUpClass(cls):
        cls.grade = 0.0
        cls.total = 0.0

    @classmethod
    def tearDownClass(cls):
        print "  Grade: ", cls.grade, " of ", cls.total

    # ------------------------------------------
    # Common tests
    # ------------------------------------------

    def solvable(self, map_name, expected):
        sx, sy, gx, gy, map, map_width, map_height = read_map(map_name)
        pathfinder = PathFinder_A_Star()
        pathfinder.solve(sx, sy, gx, gy, map, map_width, map_height)
        self.assertEqual(pathfinder.get_solvable(sx, sy, gx, gy, map, map_width, map_height), expected)

    def plan_match(self, map_name, moves):
        sx, sy, gx, gy, map, map_width, map_height = read_map(map_name)
        plan = PathFinder_A_Star().solve(sx, sy, gx, gy, map, map_width, map_height)
        self.assertEqual(plan, moves)

    def max_tree_height(self, map_name, height):
        sx, sy, gx, gy, map, map_width, map_height = read_map(map_name)
        pathfinder = PathFinder_A_Star()
        plan = pathfinder.solve(sx, sy, gx, gy, map, map_width, map_height)
        self.assertEqual(pathfinder.get_max_tree_height(sx, sy, gx, gy, map, map_width, map_height), height)

    def min_moves(self, map_name, moves):
        sx, sy, gx, gy, map, map_width, map_height = read_map(map_name)
        pathfinder = PathFinder_A_Star()
        plan = pathfinder.solve(sx, sy, gx, gy, map, map_width, map_height)
        if moves != None:
            self.assertEqual(pathfinder.get_min_moves(sx, sy, gx, gy, map, map_width, map_height), len(moves))
        else:
            self.assertEqual(pathfinder.get_min_moves(sx, sy, gx, gy, map, map_width, map_height), moves)

    # ------------------------------------------
    # Trivial
    # ------------------------------------------

    def test_trivial_solvable(self):
        self.__class__.total += TRIVIAL_GRADE
        self.solvable(TRIVIAL, True)
        self.__class__.grade += TRIVIAL_GRADE

    def test_trivial_plan_match(self):
        self.__class__.total += TRIVIAL_GRADE
        self.plan_match(TRIVIAL, TRIVIAL_SOLUTION)
        self.__class__.grade += TRIVIAL_GRADE

    def test_trivial_max_tree_height(self):
        self.__class__.total += TRIVIAL_GRADE
        self.max_tree_height(TRIVIAL, TRIVIAL_MAX_TREE_HEIGHT)
        self.__class__.grade += TRIVIAL_GRADE

    def test_trivial_min_moves(self):
        self.__class__.total += TRIVIAL_GRADE
        self.min_moves(TRIVIAL, TRIVIAL_SOLUTION)
        self.__class__.grade += TRIVIAL_GRADE

    # ------------------------------------------
    # Easy
    # ------------------------------------------

    def test_easy_solvable(self):
        self.__class__.total += EASY_GRADE
        self.solvable(EASY, True)
        self.__class__.grade += EASY_GRADE

    def test_easy_plan_match(self):
        self.__class__.total += EASY_GRADE
        self.plan_match(EASY, EASY_SOLUTION)
        self.__class__.grade += EASY_GRADE

    def test_easy_max_tree_height(self):
        self.__class__.total += EASY_GRADE
        self.max_tree_height(EASY, EASY_MAX_TREE_HEIGHT)
        self.__class__.grade += EASY_GRADE

    def test_easy_min_moves(self):
        self.__class__.total += EASY_GRADE
        self.min_moves(EASY, EASY_SOLUTION)
        self.__class__.grade += EASY_GRADE

    # ------------------------------------------
    # Medium
    # ------------------------------------------

    def test_medium_solvable(self):
        self.__class__.total += MEDIUM_GRADE
        self.solvable(MEDIUM, True)
        self.__class__.grade += MEDIUM_GRADE

    def test_medium_plan_match(self):
        self.__class__.total += MEDIUM_GRADE
        self.plan_match(MEDIUM, MEDIUM_SOLUTION)
        self.__class__.grade += MEDIUM_GRADE

    def test_medium_max_tree_height(self):
        self.__class__.total += MEDIUM_GRADE
        self.max_tree_height(MEDIUM, MEDIUM_MAX_TREE_HEIGHT)
        self.__class__.grade += MEDIUM_GRADE

    def test_medium_min_moves(self):
        self.__class__.total += MEDIUM_GRADE
        self.min_moves(MEDIUM, MEDIUM_SOLUTION)
        self.__class__.grade += MEDIUM_GRADE

if __name__ == '__main__':
    unittest.main()
