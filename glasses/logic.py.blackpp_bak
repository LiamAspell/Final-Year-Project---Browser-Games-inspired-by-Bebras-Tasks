"""
Game logic for Glasses.

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
from random import choice, sample, seed
from time import time
from typing import Any, Tuple

# CTGames framework
from ctgames.common import AnswerType, shuffle_answers

__version__ = '0.0.1'
__date__ = '2023.02.15'
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

_NUM_MCQ_ANSWERS: int = 3
"""The number of answers in each MCQ question."""

#
# Module-level names present in all games
#

SublevelBehaviour = namedtuple('SublevelBehaviour', 'rules_amount')
SublevelBehaviour.__doc__ += (
    ': NamedTuple: The complete description of the behaviour of a '
    'sublevel in the game.'
    )
SublevelBehaviour.rules_amount.__doc__ = """A positive int that specifies the
    length of the list of numbers."""


GameStateCustom = namedtuple('GameStateCustom', ('question_sequence',))
GameStateCustom.__doc__ += (
    ': NamedTuple: The game state information specific to this game, '
    'for a single player.'
    )
GameStateCustom.question_sequence.__doc__ = """list: The list of numbers."""


# Initialise the random number generator with the current time
seed(int(time()))

face_glasses_pairs = [
    ('sad', 'red'),
    ('smile', 'blue'),
    ('winking', 'white'),
    ('joyful', 'purple'),
    ('shocked', 'green'),
    ]


def create_game_round(round_behaviour: SublevelBehaviour) -> dict:
    """Create a fine-grained instance of a game round.

    Create a fine-grained instance of a game round from an arbitrary
    round behaviour namedtuple (a single instance of a game round
    without any game state information).

    Parameters
    ----------

    round_behaviour
        A namedtuple consisting of the elements required to completely
        specify a game round.

    Returns
    -------

    A dict of updates to be made to the game state, including, for
    example:

        custom : GameStateCustom
            The game state information specific to this game, for a
            single player.

    """

    # Determine the custom fields, and the correct answer
    question_sequence, target_long = _decide_on_problem_instance(
        round_behaviour
        )

    # Decide on a suitable list of multiple choice answers
    multiple_answers, targets = _decide_on_answers(
        target_long, question_sequence
        )

    # Construct a dict `updates` of keyword arguments to update the game
    # state with everything needed for a new game round.
    custom = GameStateCustom(question_sequence)
    updates = {
        'answer_type': AnswerType.MCQ,
        'multiple_answers': multiple_answers,
        'targets': targets,  # `targets` is a list of correct answers
        'custom': custom,
        }

    return updates


# ----------------------------------------------------------------------------
#
#   Local functions
#
# ----------------------------------------------------------------------------
def get_correct_answer(pairs, question):
    """
    Method to get the correct sequence of glasses corresponding to each face

    Args:
        pairs : The rules set of faces and glasses
        question : The sequence of faces in the question

    Returns:
        The correct values for the sequence of keys (pairs)
    """
    correct_answer = []
    for part in question:
        i = 0
        while i < len(pairs):
            if pairs[i][0] == part:
                correct_answer.append(pairs[i][1])
            i += 1

    return correct_answer


def replace_one_value(correct_answer, sequence):
    """
     Method to replace one value of the correct answer, as specified in the
     game

    Args:
        correct_answer : The correct answer returned from the method above
        sequence : The sequence of faces and glasses

    Returns:
        The new correct answer with one value replaced
    """
    changed = False
    replacement = random.randint(0, len(sequence) - 1)
    i = random.randint(0, len(sequence) - 2)
    while not changed:
        if correct_answer[i] != sequence[replacement][1]:
            correct_answer[i] = sequence[replacement][1]
            changed = True
        i += 1

    return correct_answer


def replace_two_values(correct_answer, sequence):
    """
     Method to replace two value of the correct answer, to create an
     incorrect answer

    Args:
        correct_answer : The fully correct answer
        sequence : The sequence of faces and glasses

    Returns:
        A randomly generated incorrect answer
    """

    incorrect_answer = copy.deepcopy(correct_answer)
    numbers = list(range(0, len(sequence)))
    random_numbers = random.sample(numbers, 2)

    values = []
    for value in sequence:
        values.append(value[1])

    values = list(correct_answer)
    for position in random_numbers:
        values.remove(correct_answer[position])
        incorrect_answer[position] = random.choice(values)

    return incorrect_answer


def get_question_sequence(pairs, rules):
    """

    Method to select the sequence of faces to go into the question
        1. Creates two lists
        2. Populates first list with rules_amount number of key-value pairs
        3. Populates second list with sequence_length amount keys
           randomly selected
        4. These two lists make up the question sequence to be returned

    Args:
        pairs : The large list of face_glasses_pairs stored at this top of
        this file
        rules : The number of rules to be displayed for this level

    Returns:
        question parts : The rules and question pieces to go into the question

    """
    print(str(pairs))
    print(str(rules))
    rules_list = copy.deepcopy(pairs)
    rule_set = []
    num_rules = 0

    while num_rules < rules:
        rule = rules_list[random.randint(0, len(rules_list) - 1)]
        rule_set.append(rule)
        rules_list.remove(rule)
        num_rules += 1
    question_list = copy.deepcopy(rule_set)
    question = []
    added_rules = 0

    while added_rules < rules:
        question_part = question_list[
            random.randint(0, len(question_list) - 1)
            ]
        question.append(question_part[0])
        question_list.remove(question_part)
        added_rules += 1
    question_parts = [rule_set, question]

    return question_parts


def _decide_on_problem_instance(round_behaviour: SublevelBehaviour) -> tuple:
    """
    Construct the data that defines the problem instance, and the answer.
    Takes the round behaviour and returns the target and the elements
    that populate the GameStateCustom for this game.

    Args:
        round_behaviour : The behaviour for the desired level

    Returns:
        question_sequence : the question for posed to the users
        target_long : the desired correct answer
    """

    rules_amount = round_behaviour.rules_amount
    pairs = copy.deepcopy(face_glasses_pairs)
    randomized_pairs = randomize_pairs(pairs)
    question_sequence = get_question_sequence(randomized_pairs, rules_amount)
    target_long = get_correct_answer(randomized_pairs, question_sequence[1])

    return question_sequence, target_long


def randomize_pairs(pairs):
    """
    Method to randomize the set of faces_glasses_pairs for any paticular
    game instance. This keeps the allocation of glasses to faces random,
    leading to more variety of outcomes.

    Args:
        pairs : Key-Value Pairs

    Returns:
        Randomized Key-Value pairs
    """
    i = 0
    keys = []
    values = []
    while i < len(pairs):
        keys.append(pairs[i][0])
        values.append(pairs[i][1])
        i += 1

    shuffle_answers(keys)
    shuffle_answers(values)
    my_list = [(keys[i], values[i]) for i in range(len(keys))]

    return my_list


def _decide_on_answers(
        target_long: Any, question_sequence: list
        ) -> Tuple[list, list]:
    """
    Decide on a suitable list of multiple choice answers.

    Args:
        target_long (int or float): The first number.


    Returns:
        The sum of the two numbers (float).

    """
    correct_answer = copy.deepcopy(target_long)
    replace_one_value(target_long, question_sequence[0])

    first_wrong_answer = replace_two_values(
        copy.deepcopy(correct_answer), question_sequence[0]
        )

    second_wrong_answer = replace_two_values(
        copy.deepcopy(correct_answer), question_sequence[0]
        )

    multiple_answers = [target_long, first_wrong_answer, second_wrong_answer]
    multiple_answers, targets = shuffle_answers(multiple_answers)

    return multiple_answers, targets
