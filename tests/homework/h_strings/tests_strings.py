import unittest

from src.homework.h_strings.strings import get_dna_complement
from src.homework.h_strings.strings import get_hamming_distance


class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        self.assertEqual(7, get_hamming_distance("GAGCCTACTAACGGGAT" , "CATCGTAATGACGGCCT")) #HW defined proof
        self.assertEqual(1, get_hamming_distance("ACGTA" , "ACGTC")) #proof that strings shorter than HW defined string will pass
        self.assertEqual(3, get_hamming_distance("TCGTA" , "TAGAC")) #proof that strings shorter than HW defined string will pass
        self.assertEqual(8, get_hamming_distance("GAGCCTACTAACGGGATCG" , "CATCGTAATGACGGCCTCC")) #proof that strings longer than HW defined string will pass

    def test_get_dna_complement(self):
        self.assertEqual("ACCGGGTTTT", get_dna_complement("AAAACCCGGT")) #HW defined proof
        self.assertEqual("AACCGGGTTTT", get_dna_complement("AAAACCCGGTT")) #proof that strings longer than HW defined string will pass
        self.assertEqual("CCTTGGAA", get_dna_complement("TTCCAAGG")) #proof that strings shorter than HW defined string will pass
        self.assertEqual("ACGT", get_dna_complement("ACGT")) #proof that strings shorter than HW defined string will pass