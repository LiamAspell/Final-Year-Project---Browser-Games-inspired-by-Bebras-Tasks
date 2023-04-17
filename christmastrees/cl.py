"""
Names specific to command-line version of game Christmas Trees.

Uses the CTGames framework. Run from directory `CTGames/bin` in a Linux
terminal using:

    python cli.py christmastrees
"""

# CTGames framework
import ctgames.christmastrees as MAIN_GAME
from ctgames.christmastrees import SublevelBehaviour
from ctgames.common import shuffle_answers
from ctgames.ctgamestypes import GameState

#
# Module-level names specific to this game
#

#
# Module-level names present in many games
#

#
# Module-level names present in all games
#

ROUND_BEHAVIOUR_RANGES: SublevelBehaviour = SublevelBehaviour(
    number_of_trees=range(4, 7)
    )
"""Specifies the allowable range of values, or type, for each parameter
of the game behaviour in a custom round defined on the command line.
Therefore, each element in this namedtuple must be either type-like (in
that it must be callable and effectively perform a cast operation) or be
sequence-like so that it can be the second parameter of an ``in``
expression."""

DEFAULT_ROUND_BEHAVIOUR: SublevelBehaviour = SublevelBehaviour(
    number_of_trees=4,
    )
"""Specifies the default value for each parameter of the game behaviour
in a custom round defined on the command line."""


def construct_cl_formatted_strings(game_state: GameState) -> dict:
    """Construct strings containing elements of the player's game state.

    The strings will be used for pretty printing the game state in a
    command line version of the game.

    Only needed if pretty printing is required. Some game state
    information is printed if the returned dict is empty (and even if
    this function is not defined at all).

    Parameters
    ----------

    game_state
        A namedtuple with the player's game state.

    Returns
    -------

    The formatted strings.
    """
    # Unpack the custom game_state values to be printed

    (tree_contents) = game_state.custom

    # Create a new dict into which the new strings will be added with
    # an appropriate key.
    formatted_strings = dict()

    return formatted_strings
