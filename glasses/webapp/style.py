from .names import GAME_BACKGROUND_FNAME

BODY_STYLE = {
    # 'backgroundColor': '...',
    'backgroundImage': 'url({{}}{})'.format(GAME_BACKGROUND_FNAME),
    'backgroundSize': 'cover',
    'backgroundRepeat': 'no-repeat',
    'backgroundPosition': 'center top',
    'backgroundAttachment': 'fixed',
    # 'backgroundBlendMode': '...'
    # See blending mode:
    # https://www.w3schools.com/cssref/pr_background-blend-mode.asp
    }
"""This will be the value of `document.body.style`."""

DIV_GAME_TOP_LEVEL_STYLE = {
    'width': '100%',
    'text-align': 'center',
    'background': 'rgba(255, 255, 255, 0.4)',
    }
"""This will be the value of `div_game_top_level.style`."""

DIV_GAME_ROUND_STYLE = {
    'background': 'rgba(255, 255, 255, 0.6)',
    'display': 'inline-block',
    'padding': '10px',
    }
"""This will be the value of `div_game_round.style`."""

DIV_ABOUT_SECTION_STYLE = {
    'background': 'rgba(255, 255, 255, 0.6)',
    'display': 'inline-block',
    }
"""This will be the value of `div_about_section.style`."""
