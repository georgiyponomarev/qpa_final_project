import unittest
from config import APP_DIR
from ddt import ddt, data
from converters import convert_dna_to_rna, convert_rna_to_protein

incorrect_input_dna = "atgce"
incorrect_input_rna = "augce"
test_cases_dna_to_rna = []
test_cases_rna_to_protein = []


# read the test data from the csv file
# the csv file contains rows with dna, rna and protein sequences
# ----------------
with open(f"{APP_DIR}/tests/test_data.csv") as file:
    first_line = True
    test_number = 1
    for line in file.read().splitlines():

        # Skip dataset header
        if first_line:
            first_line = False
            continue

        case = line.split(",")
        dna, rna, protein = case[0], case[1], case[2]
        test_cases_dna_to_rna.append((test_number, dna, rna))
        test_cases_rna_to_protein.append((test_number, rna, protein))
        
        test_number += 1

# create unit tests
# -----------------
@ddt
class ConverterTest(unittest.TestCase):
    """
    The class that creates unit tests for the two 
    converter functions: dna to rna and 
    rna to protein

    Methods
    -------
    test_convert_dna_to_rna(self, case):
        Tests the dna to rna converter function

        argument 'case' is the tuple of two strings: 
          a DNA sequence -- function input and 
          a RNA sequence -- correct output

    test_convert_rna_to_protein(self, case):
        Analogous method for testing rna to
        protein converter function

    Decorators @ddt and @data from the external
    module ddt allow to load multiple test cases.

    For the ddt documentation see:
    https://ddt.readthedocs.io/en/latest/
    """

    @data(*test_cases_dna_to_rna)
    def test_convert_dna_to_rna(self, case):
        test_number, dna, rna = case
        print(f"Testing DNA to RNA converter. Test #{test_number}")
        self.assertEqual(convert_dna_to_rna(dna), rna)

    @data(*test_cases_rna_to_protein)
    def test_convert_rna_to_protein(self, case):
        test_number, rna, protein = case
        print(f"Testing RNA to protein converter. Test #{test_number}")
        self.assertEqual(convert_rna_to_protein(rna), protein)

    def test_convert_dna_to_rna_invalid_input(self):
        print(f"Testing that dna2rna converter returns None if the input is not DNA")
        self.assertIsNone(convert_dna_to_rna(incorrect_input_dna))

    def test_convert_rna_to_protein_invalid_input(self):
        print(f"Testing that rna2protein converter returns None if the input is not RNA")
        self.assertIsNone(convert_dna_to_rna(incorrect_input_dna))


# perform unit tests
# ------------------
if __name__ == '__main__':
    unittest.main()
