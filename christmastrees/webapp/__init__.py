"""
Web app for Christmas Trees.

Uses the CTGames framework.

Designed to be imported into a server-side flask application, and
imported by a web app (using Brython).

Tested with recent versions of Python, Brython, and Firefox, on a recent
LTS version of Ubuntu, as of the date shown below.
"""
# Standard library
import random
from random import choice, randrange, shuffle

# CTGames framework
from ctgames.common import MCQ_ANSWER_LABELS
from ctgames.ctgamestypes import (
    InputDOMElementOptions,
    InputDOMElements,
    InputDOMElementType,
    TextImageSeq,
    )
from ctgames.svgcommon import SVG, create_image_from_file, create_svg_instance

from .names import IM_PATH, POSITIONS, game_state, populate_about_page

# from typing import List, Tuple
# Import List of Tuple Ints to Represent Positions

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
    'For further information go to <a target="_blank" '
    'href="https://pact.cs.nuim.ie/">pact.cs.nuim.ie</a>.'
    )

SUBSET_POSITIONS = [(50, 30)]
set_positions = [
    (200, 270),
    (135, 215),
    (75, 270),
    (195, 195),
    (135, 140),
    (70, 195),
    (180, 120),
    (135, 75),
    (95, 120),
    (165, 68),
    (105, 68),
    (135, 15),
    ]
shuffle(set_positions)

bauble_types = [
    "BlueStar",
    "Brown",
    "Cyan",
    "CyanSpiky",
    "DarkYellow",
    "DiamondPattern",
    "Purple",
    "RedTree",
    "RedSpiky",
    "Violet",
    "Yellow",
    ]
shuffle(bauble_types)
# Populate an "About..." page in the webapp
populate_about_page(developers=__credits__, date=__date__)


def _my_tree(bin_string, index, width, height):
    """
    Method to generate a tree in SVG.

    Args:
        bin_string : Sequence of lists of 0s, 1s
        index : Position of Tree in Sequence
        width : Desired Tree Width
        height : Desired Tree Height

    Returns:
        The tree to be placed on the SVG instance
    """
    list_of_svgs = []
    tree = create_image_from_file(
        id=bin_string,
        href=IM_PATH.format('tree'),
        width=width,
        height=height,
        x=index * width,
        y=0,
        )
    list_of_svgs.append(tree)
    return tree


def _my_baubles(bin_string, index, width, position, bauble_type):
    """
    Method to display baubles on the question instance

    Args:
        bin_string: List of binary values
        index: Position of tree in sequence
        width: Width of the baubles
        position: Points the bauble to correct direction
        bauble_type: Style of the bauble passed

    Returns:
        List of Baubles
    """
    baubles = []
    for pindex, bit_value in enumerate(bin_string):
        if bit_value == 1:
            bauble_id = str(bin_string) + "[" + str(index) + "]"
            bauble = create_image_from_file(
                id=bauble_id,
                href=IM_PATH.format(bauble_type[pindex] + 'Bauble'),
                width=30,
                height=30,
                x=position[pindex][0] + index * width,
                y=position[pindex][1],
                )
            baubles.append(bauble)
    return baubles


def format_problem_instance(default_text: str) -> TextImageSeq:
    """
    Create the Visual representation of the Question by returning the SVG
    representations of the Question

    Args:
        default_text

    Returns:
        TextImageSeq containing the SVG instance
    """

    number_of_trees = len(game_state.custom.tree_contents)
    tree_width = 300
    tree_height = 300
    bin_string = game_state.custom.tree_contents
    parent_width = tree_width * number_of_trees
    svg_instance = create_svg_instance(
        id='svg_instance', width=parent_width, height=tree_height
        )

    my_trees = [
        _my_tree(tree, index, tree_width, tree_height)
        for index, tree in enumerate(bin_string)
        ]

    svg_instance <= my_trees

    my_baubles = [
        _my_baubles(tree, index, tree_width, set_positions, bauble_types)
        for index, tree in enumerate(bin_string)
        ]

    svg_instance <= my_baubles
    return TextImageSeq(dom_element_seq=[svg_instance])


def format_player_answer_area() -> InputDOMElements:
    """
    Create what is necessary to allow the player to input their answer.

    Returns:
        InputDOMElements for viewing on the browser
    """

    scale_factor = 2
    number_of_trees = len(game_state.custom.tree_contents)

    tree_width = 300 / scale_factor
    tree_height = 300 / scale_factor
    parent_width = tree_width * number_of_trees
    svg_instance = create_svg_instance(
        id='svg_instance', width=parent_width, height=tree_height
        )

    mcq = [
        _create_tree_answer(game_state.multiple_answers[index])
        for index, tree in enumerate(game_state.multiple_answers)
        ]

    svg_instance <= mcq

    mcq_options = zip(MCQ_ANSWER_LABELS, mcq)
    input_dom_elements = InputDOMElements(
        dom_elem_type=InputDOMElementType.RADIOBUTTONS,
        dom_elem_options=[InputDOMElementOptions.VerticalList],
        options=mcq_options,
        )
    return input_dom_elements


def _create_baubles(tree, index):
    """
    Adds baubles into the trees in the answer

    Args:
        tree : List of binary lists
        index : Position of the tree bauble is to be mapped onto

    Returns:
        List of different baubles at different positions
    """
    answer_baubles = []
    for pindex, bit_value in enumerate(tree):
        if bit_value == 1:
            bauble_id = str(tree) + "[" + str(index) + "]"
            bauble = create_image_from_file(
                id=bauble_id,
                href=IM_PATH.format(bauble_types[pindex] + 'Bauble'),
                width=15,
                height=15,
                x=(set_positions[pindex][0] + index * 300) / 2,
                y=(set_positions[pindex][1]) / 2,
                )
            answer_baubles.append(bauble)

    return answer_baubles


def _create_tree_answer(tree) -> SVG:
    """
    Create the Visual representation of the Question by returning the SVG
    representations of the Question

    Args:
        tree : List of binary values to be represented as trees

    Returns:
        svg_instance of a sequence of trees.
    """
    svg_instance = create_svg_instance(
        id='test',
        x=0,
        y=0,
        width=150 * len(tree),
        height=150,
        )

    for index, tree in enumerate(tree):
        fname = IM_PATH.format('tree')
        svg_instance <= create_image_from_file(
            id='tree',
            x=index * 150,
            y=0,
            width=150,
            height=150,
            href=fname,
            )
        svg_instance <= _create_baubles(tree, index)

    return svg_instance
