# Standard library
import copy
import unittest

# CTGames framework
from ctgames.glasses.logic import (
    face_glasses_pairs,
    get_correct_answer,
    replace_one_value,
    replace_two_values,
    )


class TestGlasses(unittest.TestCase):
    """Testing Suite for the game Glasses"""

    def test_get_correct_answer(self):
        """Testing the method which produces the correct answer """

        question = ['shocked', 'joyful', 'sad']
        answer = ['green', 'purple', 'red']

        self.assertEqual(
            get_correct_answer(face_glasses_pairs, question), answer
            )

        question = ['sad', 'winking', 'joyful']
        answer = ['red', 'white', 'purple']

        self.assertEqual(
            get_correct_answer(face_glasses_pairs, question), answer
            )

        question = ['winking', 'joyful', 'sad', 'shocked']
        answer = ['white', 'purple', 'red', 'green']

        self.assertEqual(
            get_correct_answer(face_glasses_pairs, question), answer
            )

        question = ['joyful', 'winking', 'shocked', 'smile']
        answer = ['purple', 'white', 'green', 'blue']

        self.assertEqual(
            get_correct_answer(face_glasses_pairs, question), answer
            )

        question = ['sad', 'joyful', 'smile', 'shocked', 'winking']
        answer = ['red', 'purple', 'blue', 'green', 'white']

        self.assertEqual(
            get_correct_answer(face_glasses_pairs, question), answer
            )

        question = ['sad', 'winking', 'joyful']
        answer = ['red', 'white', 'purple']

        self.assertEqual(
            get_correct_answer(face_glasses_pairs, question), answer
            )

    def test_replace_one_value(self):
        """Testing the method responsible for creating the correct answer to be
        presented to the user"""
        question = [('shocked', 'green'), ('joyful', 'pink'), ('sad', 'red')]
        answer = ['green', 'pink', 'red']

        fully_correct = copy.deepcopy(answer)
        answer = replace_one_value(answer, question)
        correct_count = 0

        for index, element in enumerate(answer):
            if fully_correct[index] == answer[index]:
                correct_count += 1

        self.assertEqual(correct_count, len(answer) - 1)

        question = [
            ('winking', 'green'),
            ('joyful', 'red'),
            ('sad', 'purple'),
            ('smile', 'blue'),
            ]
        answer = ['green', 'red', 'purple', 'blue']

        fully_correct = copy.deepcopy(answer)
        answer = replace_one_value(answer, question)
        correct_count = 0

        for index, element in enumerate(answer):
            if fully_correct[index] == answer[index]:
                correct_count += 1

        self.assertEqual(correct_count, len(answer) - 1)

        question = [
            ('shocked', 'white'),
            ('smile', 'blue'),
            ('winking', 'purple'),
            ('sad', 'green'),
            ('joyful', 'red'),
            ]
        answer = ['white', 'blue', 'purple', 'green', 'red']

        fully_correct = copy.deepcopy(answer)
        answer = replace_one_value(answer, question)
        correct_count = 0

        for index, element in enumerate(answer):
            if fully_correct[index] == answer[index]:
                correct_count += 1

        self.assertEqual(correct_count, len(answer) - 1)

    def test_replace_two_values(self):
        """Testing the method responsible for creating incorrect answers to be
        presented to the user"""
        question = [('shocked', 'green'), ('joyful', 'pink'), ('sad', 'red')]
        answer = ['green', 'pink', 'red']

        fully_correct = copy.deepcopy(answer)
        answer = replace_two_values(answer, question)
        correct_count = 0

        for index, element in enumerate(answer):
            if fully_correct[index] == answer[index]:
                correct_count += 1

        self.assertEqual(correct_count, len(answer) - 2)

        question = [
            ('joyful', 'pink'),
            ('shocked', 'green'),
            ('smile', 'blue'),
            ('sad', 'red'),
            ]
        answer = ['pink', 'green', 'blue', 'red']

        fully_correct = copy.deepcopy(answer)
        answer = replace_two_values(answer, question)
        correct_count = 0

        for index, element in enumerate(answer):
            if fully_correct[index] == answer[index]:
                correct_count += 1

        self.assertEqual(correct_count, len(answer) - 2)

        question = [
            ('winking', 'white'),
            ('joyful', 'pink'),
            ('shocked', 'green'),
            ('smile', 'blue'),
            ('sad', 'red'),
            ]
        answer = ['white', 'pink', 'green', 'blue', 'red']

        fully_correct = copy.deepcopy(answer)
        answer = replace_two_values(answer, question)
        correct_count = 0

        for index, element in enumerate(answer):
            if fully_correct[index] == answer[index]:
                correct_count += 1

        self.assertEqual(correct_count, len(answer) - 2)
