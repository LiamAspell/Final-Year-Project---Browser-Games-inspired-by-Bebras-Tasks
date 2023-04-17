# Standard library
import unittest

# CTGames framework
from ctgames.clearingsnow.logic import (
    GameState,
    GameStateCustom,
    find_x_y,
    generate_random_arena,
    get_starting_point,
    process_input_and_solve_task,
    solve_arena,
    )

# python -m unittest clearingsnow_test.TestClearingSnow


class TestClearingSnow(unittest.TestCase):
    """
    Testing Suite for the game Clearing Snow
    """

    def test_find_x_y(self):
        """
        Test the function that takes in a game state instance and returns
        the x and y co ordinates of the symbol 'T' on the plane. The sample
        game state variables imitate the arenas used in the game.
        Tests built are to ensure the co-ordinates returned to indicate
        starting point are correct.
        """
        sample_game_state = [
            ['X', 'X', 'O', 'T'],
            ['X', 'X', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ]
        self.assertEqual(find_x_y(sample_game_state), (0, 3))

        sample_game_state = [
            ['X', 'X', 'O', 'T'],
            ['X', 'X', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ]
        self.assertEqual(find_x_y(sample_game_state), (0, 3))

        sample_game_state = [
            ['X', 'X', 'O', 'O'],
            ['X', 'X', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'T'],
            ]
        self.assertEqual(find_x_y(sample_game_state), (3, 3))

        sample_game_state = [
            ['X', 'X', 'O', 'O'],
            ['X', 'X', 'O', 'O'],
            ['O', 'T', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ]
        self.assertEqual(find_x_y(sample_game_state), (2, 1))

        sample_game_state = [
            ['X', 'X', 'O', 'X'],
            ['X', 'X', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ['O', 'T', 'O', 'O'],
            ]
        self.assertEqual(find_x_y(sample_game_state), (3, 1))

    def test_get_starting_point(self):
        """
        This method takes in the arena from data.py and updates this
        arena with the a randomized starting point. The arena is updated
        to have the character 'T' replace 'O' to indicate the starting
        point.

        Tests are to ensure returned arena is always updated
        """
        sample_game_state = [
            ['X', 'X', 'O', 'X'],
            ['X', 'X', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O'],
            ]
        returned_arena = get_starting_point(sample_game_state)
        self.assertNotEqual(sample_game_state, returned_arena)

    def test_generate_random_arena(self):
        """
        Ensuring that a random arena to the respective level will always
        return correctly
        """
        # Testing for arena of length 4
        size = 4
        test_arena = generate_random_arena(size)
        self.assertEqual(4, len(test_arena))

    def test_solve_arena(self):
        """
        Ensure that this method always returns a solved backend arena
        """
        arena = "XXOXXXOOOOOOOOOO"
        solved_arena = solve_arena(arena)
        self.assertEqual(solved_arena, "XX_XXX__________")

        arena = "OOOXOOOXOOOOXXXO"
        solved_arena = solve_arena(arena)
        self.assertEqual(solved_arena, "___X___X____XXX_")

        arena = "XXOOOOOXXXOOXXOOXOOXXOOXXOOXXXOOX"
        solved_arena = solve_arena(arena)
        self.assertEqual(solved_arena, "XX_____XXX__XX__X__XX__XX__XXX__X")

        arena = "XXXOOOOOOXXXOXXXXOOOOXXXXXOOXXXXOOOXXXOOO"
        solved_arena = solve_arena(arena)
        self.assertEqual(
            solved_arena, "XXX______XXX_XXXX____XXXXX__XXXX___XXX___"
            )

        arena = "XXOXXXOOOOOOOOOOXXOOXXXOOOXXXOOOXXOOOXOOX"
        solved_arena = solve_arena(arena)
        self.assertEqual(
            solved_arena, "XX_XXX__________XX__XXX___XXX___XX___X__X"
            )

    def test_process_input_and_solve_task(self):
        """
        Ensure this method always returns a correct answer or an
        incorrect answer based on the correctness of the input string
        """
        input_string = "EEENNNWWWSS"
        game_state = GameState(
            targets=['Congratulations, You cleared all the snow'],
            custom=GameStateCustom(
                arena=[
                    ['O', 'O', 'O', 'O'],
                    ['O', 'X', 'X', 'O'],
                    ['O', 'X', 'X', 'O'],
                    ['T', 'O', 'O', 'O'],
                    ]
                ),
            )

        result_string = process_input_and_solve_task(
            game_state, input_string, False
            )

        self.assertEqual(
            result_string.player_processed,
            "Congratulations, You cleared all the snow",
            )

        input_string = "EEENEEWWWSS"
        game_state = GameState(
            targets=['Congratulations, You cleared all the snow'],
            custom=GameStateCustom(
                arena=[
                    ['O', 'O', 'O', 'O'],
                    ['O', 'X', 'X', 'O'],
                    ['O', 'X', 'X', 'O'],
                    ['T', 'O', 'O', 'O'],
                    ]
                ),
            )

        result_string = process_input_and_solve_task(
            game_state, input_string, False
            )

        self.assertNotEqual(
            result_string.player_processed,
            "Congratulations, You cleared all the snow",
            )

        self.assertEqual(
            result_string.player_processed,
            "Your solution does not clear all snow",
            )

        input_string = "NEEESESSWWSWNNW"
        game_state = GameState(
            targets=['Congratulations, You cleared all the snow'],
            custom=GameStateCustom(
                arena=[
                    ['O', 'O', 'O', 'O', 'X'],
                    ['T', 'X', 'X', 'O', 'O'],
                    ['O', 'O', 'X', 'X', 'O'],
                    ['X', 'O', 'O', 'O', 'O'],
                    ['X', 'O', 'O', 'X', 'X'],
                    ],
                ),
            )

        result_string = process_input_and_solve_task(
            game_state, input_string, False
            )

        self.assertEqual(
            result_string.player_processed,
            "Congratulations, You cleared all the snow",
            )
