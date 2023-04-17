"""
Configuration file for the game clearingsnow.
"""

# CTGames framework
from ctgames.ctgamestypes import CTGamesProgrammerError
from ctgames.gamesbehaviour import AmbiguousValue as A  # noqa
from ctgames.gamesbehaviour import GameBehaviour
from ctgames.gamesbehaviour import LevelSublevelClass as L

from ctgames.clearingsnow import SublevelBehaviour as SB  # isort:skip

# Note, SublevelBehaviour is a namedtuple (param1, param2)
GAME_BEHAVIOUR: GameBehaviour = GameBehaviour()
"""This module-level dictionary encodes the behaviour of the game. It is 
indexed by a tuple (level, sublevel). It stores the behaviour of each 
sublevel in a `SublevelBehaviour` namedtuple."""
try:
    GAME_BEHAVIOUR.update(
        {
            L(0, 0): SB(4),
            L(0, 1): SB(4),
            L(0, 2): SB(4),
            L(1, 0): SB(5),
            L(1, 1): SB(5),
            L(1, 2): SB(5),
            L(2, 0): SB(6),
            L(2, 1): SB(6),
            L(2, 2): SB(6),
            }
        )
except (TypeError, ValueError):
    raise CTGamesProgrammerError('Invalid `GAME_BEHAVIOUR` in behaviour.py.')
