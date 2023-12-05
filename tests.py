import unittest
import logic
import cli


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        """
        Test 7: the correct game winner, if one exists, is detected
        """
        # put all the test boards in the board_list and put all the results in the expect_winners
        board_list = [
            [
                ['X', None, 'O'],
                [None, 'X', None],
                [None, 'O', 'X'],
            ],
            [
                ['X', 'X', 'X'],

                ['O', None, 'O'],

                ['O', 'O', 'X'],
            ],
            [
                ['X', 'O', 'X'],

                ['O', 'O', 'O'],

                ['O', 'X', 'X'],
            ],
            [
                ['O', 'O', 'X'],

                ['O', 'X', 'O'],

                ['O', None, 'O'],
            ],
            [
                ['X', 'O', 'X'],

                ['O', 'X', 'O'],

                ['O', 'X', 'O'],
            ],
            [
                ['X', 'O', 'X'],

                ['X', None, None],

                ['X', None, None],

            ],
            [
                ['X', 'O', 'O'],

                [None, 'O', None],

                [None, 'O', None],
            ],
            [
                ['X', None, 'O'],

                [None, None, 'O'],

                ['O', None, 'O'],

            ],
            [
                [None, None, None],

                [None, None, None],

                [None, None, None],
             ],

            [
                ['X', None, 'X'],

                [None, 'X', 'O'],

                ['X', 'O', 'X'],
            ],
            [
                ['O', 'X', 'O'],

                [None, 'O', 'O'],

                ['X', 'X', 'O']
            ]
        ]
        expect_winners = [
            ('X', 'D'),
            ('X', 'H'),
            ('O', 'H'),
            ('O', 'V'),
            (None, None),
            ('X', 'V'),
            ('O', 'V'),
            ('O', 'V'),
            (None, None),
            ('X', 'D'),
            ('O', 'V')
             ]
        for i in range(0, len(board_list)):
            self.assertEqual(logic.get_winner(board_list[i]), expect_winners[i])

    def test_check_winner_horizontal(self):
        """
        Test 5: winning end of the games detected in horizontal direction
        """
        board = [
            ['X', 'X', 'X'],
            ['O', 'X', 'O'],
            [None, None, 'O'],
        ]
        self.assertEqual(logic.get_winner(board), ('X', 'H'))

    def test_check_winner_vertical(self):
        """
        Test 5: winning end of the games detected in vertical direction
        """
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['X', None, None],
        ]
        self.assertEqual(logic.get_winner(board), ('X', 'V'))

    def test_check_winner_diagonal(self):
        """
        Test 5: winning end of the games detected in diagonal direction
        """
        board = [
            ['X', 'O', 'X'],
            [None, 'X', 'O'],
            ['O', None, 'X'],
        ]
        self.assertEqual(logic.get_winner(board), ('X', 'D'))

    def test_check_winner_draw(self):
        """
        Test 5: draw games are identified
        """
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), (None, None))

    def test_make_empty_board(self):
        """
        Test 1: the game is initialized with an empty board
        """
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), board)

    def test_other_player(self):
        """
        Test 4: after one player plays, the other player has a turn
        """
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

    def test_location_is_valid(self):
        """
        Test 6: players can play only in viable spots
        """
        board_test = [
            ['X', None, 'X'],

            [None, 'X', 'O'],

            ['X', 'O', 'X'],
        ]
        # Test if the input is a valid integer number between 1-9 whose location in the board is None.
        # W is not a number, it's invalid.
        self.assertEqual(logic.location_is_valid(board_test, 'W'), False)
        # 2.5 id not an integer number, it's invalid.
        self.assertEqual(logic.location_is_valid(board_test, '2.5'), False)
        # 2 is a valid integer number.
        self.assertEqual(logic.location_is_valid(board_test, '2'), True)
        # 1's location is not None, it's invalid.
        self.assertEqual(logic.location_is_valid(board_test, '1'), False)
        # 0 and 10 is not between 1-9, they are invalid.
        self.assertEqual(logic.location_is_valid(board_test, '0'), False)
        self.assertEqual(logic.location_is_valid(board_test, '10'), False)

    def test_chose_mode(self):
        """
        Test 2: the game is initialized with either 2 players (human-human) or 1 player (human-bot)
        """
        test_game = cli.TicTacToc()
        test_game.chose_mode(1)
        self.assertEqual(test_game.is_single_player, True)
        test_game.chose_mode(2)
        self.assertEqual(test_game.is_single_player, False)

    def test_identify_player(self):
        """
        Test 3: players are assigned a unique piece to play: X or O
        """
        test_game = cli.TicTacToc()
        test_game.chose_mode(1)
        test_game.player_priority('Y')
        self.assertEqual(test_game.player_1, 'X')
        self.assertEqual(test_game.bot, 'O')
        test_game.player_priority('n')
        self.assertEqual(test_game.bot, 'X')
        self.assertEqual(test_game.player_1, 'O')
        test_game.chose_mode(2)
        self.assertEqual(test_game.player_1, 'X')
        self.assertEqual(test_game.player_2, 'O')


if __name__ == '__main__':
    unittest.main()
