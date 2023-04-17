"""Stub script file that is called directly by the HTML-embedded
Python.

This file will be called in the special case of a standalone version of
the game (during development).

On 5.12.2016, TN felt a special stub file was necessary so that the
game-specific Brython code can be accessible from the framework as an
imported module (it seems that .py files called directly from the HTML
file are run as scripts and do not appear in the `sys.modules`
dictionary).
"""
from ctgames.framework import create_gui_elements, go_to_standalone_game_list
from ctgames.player import simulate_anonymous_sign_in
from ctgames.glasses.text_constants import MODULE_NAME
import ctgames.glasses.webapp
import ctgames.glasses.webapp.style

_bry_module_name = 'ctgames.{}.webapp'.format(MODULE_NAME)

# Simulate the sign in process by a player (there are no signs in for
# standalone games).
simulate_anonymous_sign_in()

# Update the "Return to game menu" function in `ctgames.framework` for
# this special standalone game. The other place this is done is in the
# `ctgames.gamemenu` module. We do it this way because we do not want
# the `ctgames.framework` module to import this module and thus cause a
# circular reference.
ctgames.framework.GAME_MENU_FUNCTION = go_to_standalone_game_list

# Create various GUI elements (e.g. buttons) and display the main top-level
# screen.
create_gui_elements(_bry_module_name)
