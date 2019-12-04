# test cases for MynesBoard

from Pod7.MynesBoard import MynesBoard
import unittest


class MyneBoardTestCase(unittest.TestCase):

    def test_board_default(self):
        """
        Test if the default values of the board's attributes are correct
        """
        test_board = MynesBoard()
        self.assertEqual(test_board.width, 8)
        self.assertEqual(test_board.height, 8)
        self.assertEqual(test_board.mine_count, 10)

    def test_mine_count(self):
        """
        Test if the actual number of mine distributed is the same as the
        default mine count
        """
        test_board = MynesBoard()
        count = 0
        for x in range(test_board.width):
            for y in range(test_board.height):
                if test_board.board[y][x].value == -1:
                    count += 1
        self.assertEqual(count, test_board.mine_count)

    def test_square_number_correct(self):
        """
        Randomly choose one square which is not Mine or Empty and count
        the number of mines around the square. Test if the number we count
        is the same as the number on this square.
        """
        # Since there is no number on any square now, this test will be
        # completed later.
        pass


if __name__ == '__main__':
    unittest.main()
