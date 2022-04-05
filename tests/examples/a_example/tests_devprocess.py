import unittest

from src.examples.a_example.devprocess import use_local_variable

class Test_Config(unittest.TestCase):

    def use_local_variable(self):
        self.assertEqual(100, use_local_variable(100))

