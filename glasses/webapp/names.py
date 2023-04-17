"""This module is used for CTGames web app features such as this game's
tutorial and "About..." page, and to define web app -related constants."""

# Standard library
from random import seed
from time import time
from typing import List, Optional

# CTGames framework
from ctgames.common import generate_about_text
from ctgames.ctgamestypes import GameState, TextImageSeq
from ctgames.framework import DisplayType
from ctgames.librarydom import IM_PATH_TEMPLATE

from ctgames.glasses import GAME_NAME, MODULE_NAME  # isort:skip

#
# Module-level names specific to this game
#


#
# Module-level names relevant to all games
#

GAME_LOGO_FNAME = 'game_logo.png'
"""The filename of the logo that appears at the top of each game round.
The logo should graphically display the game name."""

GAME_ICON_FNAME = 'game_icon.svg'
"""The filename of a small picture that represents the game in the game
menu."""

GAME_BACKGROUND_FNAME = 'background.svg'
"""The name plus extension of the background image. The path should not
be specified."""

ABOUT_COMPATIBILITY, ABOUT_DEVELOPERS, ACKNOWLEDGEMENTS = None, None, None
"""Three names that must be populated for the webapp "About..." page."""

GAME_DISPLAY_TYPE: bool = DisplayType.SVG
"""Whether the game is based on SVG images or not. Accessed by the
CTGames framework."""

_IM_EXT = '.svg'
"""Graphic filename extension."""

IM_PATH: str = IM_PATH_TEMPLATE.format(MODULE_NAME, '{}', _IM_EXT)
"""The path in which images for this game can be found, parameterised by
the image's filename."""

WORKBOOK_GRAPHIC_IDS: dict = {
    'rules': [],
    'round': [],
    }
"""The ids of the graphical game elements that need to be extracted from
each game round for the construction of workbooks."""

game_state: Optional[GameState] = None
"""The game state of the current player, held locally and passed back
and  forth to the game logic file, and referred to by the CTGames
framework."""

# Initialise the random number generator with the current time
seed(int(time()))


#
# About page
#


def populate_about_page(developers: List[str], date: str) -> None:
    """Set up the names the framework uses to create the webapp "About" page.

    Function will be called by webapp/__init__.py when it defines the
    credits and date.
    """
    global ABOUT_COMPATIBILITY, ABOUT_DEVELOPERS, ACKNOWLEDGEMENTS
    tuple_ = generate_about_text(
        game_name=GAME_NAME,
        developers=developers,
        logo=['cooltext'],
        images=['pixabay', 'openclipart'],
        date=date,
        )
    ABOUT_COMPATIBILITY, ABOUT_DEVELOPERS, ACKNOWLEDGEMENTS = tuple_


#
# Tutorial
#

# Add your tutorial here!
_TUT_IM_HEIGHT = 150
"""We only specify the height of each image and let the browser
determine the width from the image."""

_TUT_PATH: str = IM_PATH_TEMPLATE.format(MODULE_NAME, '{}', '.svg')
"""The path in which images for the tutorial can be found, parameterised
by the image's filename."""

_TUT_TEXT_SEQ = [
    '''In Glasses, different facial expressions match different styles 
    of glasses. You must match the facial expressions to their respective 
    glasses, and select the sequence of glasses where the fewest faces 
    wear the wrong glasses \n\n''',
    '''<br /> \nIn the below question, the selected 
    answer is the correct one, as the fewest amount of faces are matched
    to an incorrect set of glasses
    ''',
    ]

_TUT_IM_FNAMES = ['Instruction1', 'Instruction2']
_TUT_IM_SEQ = [_TUT_PATH.format(fn) if fn else fn for fn in _TUT_IM_FNAMES]

TUTORIAL_TEXT_IM_SEQ = TextImageSeq(
    text_seq=_TUT_TEXT_SEQ,
    im_seq=_TUT_IM_SEQ,
    im_height=[125, 600],
    )
"""The object used to populate the tutorial section of this game."""
