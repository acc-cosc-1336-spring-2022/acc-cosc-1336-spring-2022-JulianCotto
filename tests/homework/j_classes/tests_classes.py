import unittest

from src.homework.j_classes import class_a

class Test_Config(unittest.TestCase):

    def test_dice_roll_1(self):
        die = class_a.Die()
        die.roll()
        if die.get_roll_value() in [1, 2, 3, 4, 5, 6]:
            RealRoll = True
        else:
            RealRoll = False
        self.assertEqual(True, RealRoll)

    def test_dice_roll_2(self):
        my_die = class_a.Die()
        my_die.roll()
        if my_die.get_roll_value() in [1, 2, 3, 4, 5, 6]:
            RealRoll = True
        else:
            RealRoll = False
        self.assertEqual(True, RealRoll)

    def test_dice_roll_3(self):
        the_die = class_a.Die()
        the_die.roll()
        if the_die.get_roll_value() in [1, 2, 3, 4, 5, 6]:
            RealRoll = True
        else:
            RealRoll = False
        self.assertEqual(True, RealRoll)

    def test_dice_roll_fail(self):
        a_die = class_a.Die()
        a_die.roll()
        if a_die.get_roll_value() in [7, 8, 9, 10, 11, 12]:
            RealRoll = True
        else:
            RealRoll = False
        self.assertEqual(False, RealRoll)
