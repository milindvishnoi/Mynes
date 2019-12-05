# test cases for MyneSquare

from Pod7.MyneSquare import MyneSquare
import pygame
import unittest


class MyneSquareTestCase(unittest.TestCase):

    def test_myne_creation(self):
        """
        test if the MyneSquare is created successfully and if all attributes
        are assigned correctly
        """
        test_myne = MyneSquare(-1, False, "temp_mine.png",
                               pygame.Rect(1, 2, 1, 2))
        self.assertEqual(test_myne.value, -1)
        self.assertEqual(test_myne.flag, False)
        # last assertion need to be discussed later
        self.assertEqual(test_myne.hitbox, pygame.Rect(1, 2, 1, 2))


if __name__ == '__main__':
    unittest.main()
