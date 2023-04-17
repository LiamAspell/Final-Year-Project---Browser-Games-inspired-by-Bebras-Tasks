"""
Game logic for Christmas Trees.

Uses the CTGames framework.

Designed to be imported and run on the command line, imported into a
server-side flask application, imported by a mobile app (using Kivy),
and imported by a web app (using Brython).

Tested with recent versions of Python, Brython, and Firefox, on a recent
LTS version of Ubuntu, as of the date shown below.
"""

# Standard library
import copy
import random
from collections import namedtuple
from random import seed, shuffle
from time import time
from typing import Any, Tuple

# CTGames framework
from ctgames.common import AnswerType, shuffle_answers

__version__ = '0.0.1'
__date__ = '2022.11.03'
__copyright__ = 'Copyright 2023, Thomas J. Naughton'
__credits__ = ['Liam Aspell', 'Thomas J. Naughton']
__license__ = 'Proprietary'
__contact__ = 'Thomas J. Naughton'
__email__ = 'tomn@cs.nuim.ie'
__status__ = 'Development'  # 'Prototype', 'Development', or 'Production'
__about__ = (
    'Written as part of the Maynooth University PACT initiative to '
    'teach computer science/computational thinking to schoolchildren. '
    'For further information go to https://pact.cs.nuim.ie .'
    )

#
# Module-level names specific to this game
#

_NUM_MCQ_ANSWERS: int = 4
"""The number of answers in each MCQ question."""
#
# Module-level names present in all games
#
SublevelBehaviour = namedtuple('SublevelBehaviour', 'number_of_trees')
SublevelBehaviour.__doc__ += (
    ': NamedTuple: The complete description of the behaviour of a '
    'sublevel in the game.'
    )

SublevelBehaviour.number_of_trees.__doc__ = """A positive int that specifies 
the number of trees in the sequence of the specific question."""


GameStateCustom = namedtuple('GameStateCustom', ('tree_contents',))
GameStateCustom.__doc__ += (
    ': NamedTuple: The game state information specific to this game, '
    'for a single player.'
    )
GameStateCustom.tree_contents.__doc__ = """The list of binary values 
representing decorations on the tree """


# Initialise the random number generator with the current time
seed(int(time()))


def create_game_round(round_behaviour: SublevelBehaviour) -> dict:
    """
    Method to create a game round based on the behaviour parameters
    """
    tree_contents, target_long = _decide_on_problem_instance(round_behaviour)
    multiple_answers, targets = _decide_on_answers(target_long, tree_contents)
    custom = GameStateCustom(tree_contents)

    # 5. Construct a dict `updates` of keyword arguments to update the game
    updates = {
        'answer_type': AnswerType.MCQ,
        'multiple_answers': multiple_answers,
        'targets': targets,
        'custom': custom,
        }

    return updates


# ----------------------------------------------------------------------------
#
#   Local functions
#
# ----------------------------------------------------------------------------


def build_tree_sequence(trees):
    """
    Method to create a list of lists containing binary values

    Args:
       trees : The amount of trees for this paticular level

    Returns:
        tree_sequence : A randomized set of lists representing trees on the
        backend
    """
    tree_sequence = []
    baubles = trees + 1
    current_tree = [0] * baubles
    count = 0
    while count != trees + 1:
        random_var = random.randrange(0, baubles, 1)
        if current_tree[random_var] == 0:
            current_tree[random_var] = 1
            copied = current_tree.copy()
            if count != 0:
                tree_sequence.append(copied)
        else:
            boolean = False
            while not boolean:
                random_var_2 = random.randrange(0, baubles, 1)
                if current_tree[random_var_2] == 0:
                    current_tree[random_var_2] = 1
                    z = current_tree.copy()
                    if count != 0:
                        tree_sequence.append(z)

                    boolean = True
        count += 1
    return tree_sequence


def get_correct_answer(temp):
    """
    Method to generate the correct answer when given an unsorted list of trees

    Args:
        temp : the unsorted list of trees

    Returns:
        correct_answer : the correct answer (Sorted list based on sum)
    """
    correct_answer = temp
    for element in range(len(correct_answer)):
        for j in range(0, len(correct_answer) - 1):
            if sum(correct_answer[j]) > sum(correct_answer[j + 1]):
                temp = correct_answer[j]
                correct_answer[j] = correct_answer[j + 1]
                correct_answer[j + 1] = temp
    return correct_answer


def _decide_on_problem_instance(round_behaviour: SublevelBehaviour) -> tuple:
    """
    Method to generate elements of the problem instance

    Args:
        round_behaviour : The round level specific behaviour

    Returns:
        tree_contents : contents of the question list
        target_long : the sorted list of trees (correct answer)
    """
    # Generate the game Sequence
    number_of_trees = round_behaviour.number_of_trees
    tree_contents = build_tree_sequence(number_of_trees)

    # Generate the correct Answer
    temp = copy.copy(tree_contents)
    target_long = get_correct_answer(temp)

    # Ensuring tree_contents does not equal the correct answer
    if tree_contents == target_long:
        shuffle(tree_contents)
    if tree_contents == target_long:
        tree_contents[:2] = reversed(tree_contents[:2])
    return tree_contents, target_long


def _decide_on_answers(
        target_long: Any, tree_contents: list
        ) -> Tuple[list, list]:
    """
    Method to generate correct and incorrect answer, and verify no
    duplicates are displayed

    Args:
        target_long : the correct answer
        tree_contents : the question sequence

    Returns:
        multiple_answers: Incorrect answers to make up the MCQ game
        targets : The correct answer
    """

    incorrect_answer_1 = copy.copy(tree_contents)
    random.shuffle(incorrect_answer_1)

    if incorrect_answer_1 == target_long:
        while incorrect_answer_1 == target_long:
            shuffle_answers(incorrect_answer_1)

    incorrect_answer_2 = copy.copy(incorrect_answer_1)
    random.shuffle(incorrect_answer_2)
    if incorrect_answer_2 == target_long:
        while incorrect_answer_2 == target_long:
            shuffle_answers(incorrect_answer_2)

    if incorrect_answer_1 == incorrect_answer_2:
        while incorrect_answer_1 == incorrect_answer_2:
            shuffle_answers(incorrect_answer_2)

    multiple_answers = [target_long, incorrect_answer_1, incorrect_answer_2]
    multiple_answers, targets = shuffle_answers(multiple_answers)

    return multiple_answers, targets
