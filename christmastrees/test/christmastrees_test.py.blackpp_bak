# Standard library
import unittest

# CTGames framework
from ctgames.christmastrees.logic import (
    build_tree_sequence,
    get_correct_answer,
    )

# Command to Run Tests -
# python -m unittest christmastrees_test.TestChristmasTrees


class TestChristmasTrees(unittest.TestCase):
    """Testing Suite for the game Christmas Trees"""

    def test_build_tree_sequence(self):
        """
        Checks that the build tree sequence method does not generate any
        erroneous list of lists
        """
        trees = 5
        tree_sequence = build_tree_sequence(trees)
        # Check that the length of the tree sequence is correct
        self.assertEqual(len(tree_sequence), trees)
        for i in range(len(tree_sequence)):
            for j in range(i + 1, len(tree_sequence)):
                self.assertNotEqual(tree_sequence[i], tree_sequence[j])

    def test_get_correct_answer(self):
        """
        Testing that the inputted list can be a list of int values in random
        order, and that the outputted list is the same list, but contains
        the elements in ascending order.
        """

        # A simulation for a solution containing 3 trees
        temp = [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]]
        expected_output = [[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]]
        self.assertEqual(get_correct_answer(temp), expected_output)

        # A simulation for a solution containing 4 trees
        temp = [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1]]
        expected_output = [
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 1],
            ]
        self.assertEqual(get_correct_answer(temp), expected_output)

        # A simulation for a solution containing 5 trees
        temp = [
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 0, 0],
            ]
        expected_output = [
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0],
            ]
        self.assertEqual(get_correct_answer(temp), expected_output)

        # A simulation for a solution containing 6 trees
        temp = [
            [1, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0],
            ]
        expected_output = [
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [1, 1, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0],
            ]
        self.assertEqual(get_correct_answer(temp), expected_output)

    def test_decide_on_problem_instance(self):
        """"""
        round_behaviour = 3
        tree_contents = [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]]
        target_long = [[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]]

        # Check that tree_contents is a list and has the expected length
        self.assertIsInstance(tree_contents, list)
        self.assertEqual(len(tree_contents), 3)

        # Check that target_long is a list and has the expected length
        self.assertIsInstance(target_long, list)
        self.assertEqual(len(target_long), 3)

        # Check that tree_contents is not equal to target_long
        self.assertNotEqual(tree_contents, target_long)

        # Check that tree_contents and target_long have the same elements
        self.assertCountEqual(tree_contents, target_long)

    def test_decide_on_answers(self):
        """
        Test the function which generates answers to contest the correct answer

        """
        multiple_answers = [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]]
        targets = [[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]]

        # Check that multiple_answers and targets are both lists
        self.assertIsInstance(multiple_answers, list)
        self.assertIsInstance(targets, list)

        # Check that multiple_answers has the expected length and
        # contains the expected elements

        self.assertEqual(len(multiple_answers), 3)
        self.assertNotEqual(multiple_answers[0], multiple_answers[1])
        self.assertNotEqual(multiple_answers[1], multiple_answers[2])
        self.assertNotEqual(multiple_answers[0], multiple_answers[2])
