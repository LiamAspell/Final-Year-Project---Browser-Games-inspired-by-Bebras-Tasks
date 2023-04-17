"""Text constants to be used in the game Glasses.
"""

GAME_NAME: str = 'Glasses'
"""The name of the game in title case."""

MODULE_NAME: str = 'glasses'
"""The module name for the game in the `ctgames` namespace."""

GAME_INSTRUCTIONS_TEACHERS: str = '''\
        Different facial expressions match different glasses. The player is 
        presented with a sequence of face/glasses pairs, and a question 
        sequence of faces, and most determine the sequence of glasses which 
        the most amount of faces wear correct glasses.'''
"""A generic game help message (could be used for command line or
graphical versions of the game). Intended to be read by teachers."""

GAME_QUESTION_CHILDREN: str = (
    'Find the option where the fewest faces wear the wrong glasses'
    )
"""A very simple game question that can be understood by a child."""

GAME_INSTRUCTIONS_CHILDREN: str = '''\
        Using the rules given, select the answer with the most amount of 
        matching glasses to faces in the question'''
"""Very simple game instructions that can be understood by a child."""

SCIENCE_FACT_CHILDREN: str = '''\
        Glasses or contact lenses correct vision because they allow the eye to focus light in the right spot on the retina — the spot that produces the clearest image. '''
"""Nature or science fact related to the game, suitable for children."""
