import unittest

from src.homework.h_strings.strings import get_dna_complement
from src.homework.h_strings.strings import get_hamming_distance


class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        self.assertEqual(7, get_hamming_distance("GAGCCTACTAACGGGAT" , "CATCGTAATGACGGCCT"))
        self.assertEqual(1, get_hamming_distance("ACGTA" , "ACGTC"))
        self.assertEqual(3, get_hamming_distance("TCGTA" , "TAGAC"))

    def test_get_dna_complement(self):
        self.assertEqual("ACCGGGTTTT", get_dna_complement("AAAACCCGGT"))
        self.assertEqual("CCTTGGAA", get_dna_complement("TTCCAAGG"))
        self.assertEqual("ACGT", get_dna_complement("ACGT"))