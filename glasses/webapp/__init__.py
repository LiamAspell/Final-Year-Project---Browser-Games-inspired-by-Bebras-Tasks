"""
Web app for Glasses.

Uses the CTGames framework.

Designed to be imported into a server-side flask application, and
imported by a web app (using Brython).

Tested with recent versions of Python, Brython, and Firefox, on a recent
LTS version of Ubuntu, as of the date shown below.
"""

# CTGames framework
from ctgames.common import MCQ_ANSWER_LABELS
from ctgames.ctgamestypes import (
    InputDOMElementOptions,
    InputDOMElements,
    InputDOMElementType,
    TextImageSeq,
    )
from ctgames.framework import new_text_image_seq
from ctgames.svgcommon import SVG, create_image_from_file, create_svg_instance

from .names import IM_PATH, game_state, populate_about_page

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
    'For further information go to <a target="_blank" '
    'href="https://pact.cs.nuim.ie/">pact.cs.nuim.ie</a>.'
    )

# Populate an "About..." page in the webapp
populate_about_page(developers=__credits__, date=__date__)


def _my_rules(faces, index, width, height):
    """
    Method to create the faces to represent the rules in a game instance
    Returns an svg file to the format_problem_instance() method

    Args:
        faces : Desired SVG file
        index : Position of the SVG in the rules sequence
        width : Desired SVG Width
        height: Desired SVG Height

    Returns:
        SVG face to go into the rules set

    """
    face = create_image_from_file(
        id=faces,
        href=IM_PATH.format(faces[0]),
        width=width,
        height=height,
        x=index * width,
        y=100,
        )

    return face


def _my_question_faces(faces, index, width, height):
    """
    Returns an svg instance of a face to go in the question instance set

    Args:
        faces : the SVG asset to be used
        index : the position of the face in the sequence
        width : desired SVG width
        height : desired SVG height

    Returns:
        An SVG image of a face to make up a paticular question
    """
    face = create_image_from_file(
        id=faces,
        href=IM_PATH.format(faces),
        width=width,
        height=height * 3,
        x=index * width,
        y=200,
        )

    return face


def _add_glasses(glasses, index, width, height):
    """
    This method returns a glasses svg to the question.

    Args:
        glasses : The pair of glasses SVG file to use
        index : Desired position in order for SVG
        width : Desired width of SVG
        height : Desired height of SVG

    Returns:
        Glasses SVG asset
    """
    glasses = create_image_from_file(
        id=glasses,
        href=IM_PATH.format(glasses[1]),
        width=width,
        height=height,
        x=14 + (index * 125),
        y=100,
        )

    return glasses


def _add_answer_glasses(glasses, width) -> SVG:
    """
    Method to add glasses to each answer

     Args:
        glasses: The set of glasses to go into the answer
        width: Desired width of the glasses

    Returns:
        SVG Instance containing glasses
    """
    sequence_length = len(glasses)
    svg_width = sequence_length * 150
    svg_height = 110

    svg_instance = create_svg_instance(
        id="Glasses",
        x=0,
        y=0,
        width=svg_width,
        height=svg_height,
        )

    background = create_image_from_file(
        id="Background",
        href=IM_PATH.format('backing'),
        x=0,
        y=0,
        width=svg_width,
        height=svg_height,
        )
    svg_instance <= background

    position = 0
    while position < len(glasses):
        image = create_image_from_file(
            id=glasses[position],
            href=IM_PATH.format(glasses[position]),
            width=width,
            height=30,
            x=150 * position,
            y=40,
            )
        svg_instance <= image
        position += 1

    return svg_instance


def format_problem_instance(default_text: str) -> TextImageSeq:
    """
    Create the Visual representation of the Question by returning the SVG
    representations of the Question

    Returns:
        TextImageSeq containing an svg instance with the SVG version of the
        problem
    """
    rules_faces = game_state.custom.question_sequence[0]
    rules_face_count = len(game_state.custom.question_sequence[0])
    face_width = 125
    face_height = 125
    parent_width = face_width * rules_face_count

    svg_instance = create_svg_instance(
        id='svg_instance', width=parent_width, height=500
        )

    rules_text = create_image_from_file(
        id="Rules String",
        href=IM_PATH.format('TheRulesAre'),
        width=200,
        height=100,
        x=0,
        y=0,
        )
    svg_instance <= rules_text

    my_rules = [
        _my_rules(face, index, face_width, face_height)
        for index, face in enumerate(rules_faces)
        ]
    svg_instance <= my_rules

    rules_glasses = []
    for index, colour in enumerate(game_state.custom.question_sequence[0]):
        rules_glasses.append(game_state.custom.question_sequence[0][index])
    my_glasses = [
        _add_glasses(face, index, 100, 100)
        for index, face in enumerate(rules_glasses)
        ]
    svg_instance <= my_glasses

    question_text = create_image_from_file(
        id="Question String",
        href=IM_PATH.format('TheQuestionIs'),
        width=200,
        height=100,
        x=0,
        y=250,
        )
    svg_instance <= question_text

    question_faces = game_state.custom.question_sequence[1]
    my_question_faces = [
        _my_question_faces(tree, index, face_height, face_width)
        for index, tree in enumerate(question_faces)
        ]
    svg_instance <= my_question_faces

    return TextImageSeq(dom_element_seq=[svg_instance])


def format_player_answer_area() -> InputDOMElements:
    """
    Create what is necessary to allow the player to input their answer.

    Returns:
        InputDOMElements containing
    """
    svg_instance = create_svg_instance(
        id='svg_instance', width=400, height=200
        )

    mcq = [
        _add_answer_glasses(
            game_state.multiple_answers[index],
            140,
            )
        for index, seq in enumerate(game_state.multiple_answers)
        ]
    svg_instance <= mcq

    mcq_options = zip(MCQ_ANSWER_LABELS, mcq)
    input_dom_elements = InputDOMElements(
        dom_elem_type=InputDOMElementType.RADIOBUTTONS,
        dom_elem_options=[InputDOMElementOptions.VerticalList],
        options=mcq_options,
        )

    return input_dom_elements
