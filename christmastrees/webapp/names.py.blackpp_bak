"""This module is used for CTGames web app features such as this game's
tutorial and "About..." page, and to define web app -related constants."""

# Standard library
from random import seed
from time import time
from typing import List, Optional, Tuple

# CTGames framework
from ctgames.christmastrees import GAME_NAME, MODULE_NAME
from ctgames.common import generate_about_text
from ctgames.ctgamestypes import GameState, TextImageSeq
from ctgames.framework import DisplayType
from ctgames.librarydom import IM_PATH_TEMPLATE

#
# Module-level names specific to this game
#

POSITIONS: List[Tuple[int]] = [
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

#
# Module-level names relevant to all games
#

GAME_LOGO_FNAME = 'game_logo.png'
"""The filename of the logo that appears at the top of each game round.
The logo should graphically display the game name."""

GAME_ICON_FNAME = 'game_icon.svg'
"""The filename of a small picture that represents the game in the game
menu."""

GAME_BACKGROUND_FNAME = 'background.jpg'
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
_TUT_IM_HEIGHT = 250
"""We only specify the height of each image and let the browser
determine the width from the image."""

_TUT_PATH: str = IM_PATH_TEMPLATE.format(MODULE_NAME, '{}', '.svg')
"""The path in which images for the tutorial can be found, parameterised
by the image's filename."""

_TUT_TEXT_SEQ = [
    '''In christmas trees, you are presented with a sequence of trees 
    with different levels of decoration. In order to win, you must 
    select the correct order that the tree was decorated.\n\n''',
    '''\n\nThe trees will vary in decoration from the empty tree above to the
    decorated tree below.\n\n''',
    ]

_TUT_IM_FNAMES = ['tree', 'Decorated Tree']
_TUT_IM_SEQ = [_TUT_PATH.format(fn) if fn else fn for fn in _TUT_IM_FNAMES]

TUTORIAL_TEXT_IM_SEQ = TextImageSeq(
    text_seq=_TUT_TEXT_SEQ,
    im_seq=_TUT_IM_SEQ,
    im_height=_TUT_IM_HEIGHT,
    )
"""The object used to populate the tutorial section of this game."""
