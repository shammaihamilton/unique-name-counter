import unittest
from name_processor import NameProcessor


class TestNameProcessor(unittest.TestCase):
    def setUp(self):
        self.name_processor = NameProcessor()

    def test_simple_check_by_remove_space(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah  ", " Egli", "Deborah ", " Egli", " Deborah Egli "), 1)

    def test_first_name_with_middle_name_and_2_last_names(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah lea", "Egli levi", "Deborah lea", "Egli levi", "Egli levi Deborah lea"), 1)

    def test_one_first_name_2_last_names_and_middle_name_in_card(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah", "Egli levi", "Deborah", "Egli levi", "Egli levi Deborah lea"), 1)

    def test_two_last_names_first_name_first_in_card(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah", "Egli levi", "Deborah", "Egli levi", "Egli levi Deborah"), 1)

    def test_extra_character_to_remove(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah S", "Egli levi r", "t Deborah", "Egli levi", "Egli levi Deborah"), 1)

    def test_two_first_names_one_last_name(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah lea", "levi", "Deborah lea", "levi", "levi Deborah lea"), 1)

    def test_spelling_check_in_first_name(self):
        self.assertEqual(self.name_processor.count_unique_names("Deboah lea", "levi", "Deborah lea", "levi", "levi Debrah lea"), 1)

    def test_spelling_in_middle_first_last_names(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah le", "levi", "Deboah lea", "lei", "levi Deborh lea"), 1)

    def test_two_different_first_names(self):
        self.assertEqual(
            self.name_processor.count_unique_names("Michele", "Egli", "Deborah", "Egli", "Michele Egli"), 2)

    def test_all_different_first_names(self):
        self.assertEqual(
            self.name_processor.count_unique_names("Michele", "Egli", "Deborah", "Egli", "shammai Egli"), 3)

    def test_different_last_names(self):
        self.assertEqual(self.name_processor.count_unique_names("Michele", "Egli", "Deborah", "Houri", "Michele Hamilton"), 3)

    def test_nicknames_for_same_person(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli"), 1)

    def test_extra_character(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah S", "Egli t", "y Deborah", " u Egli", "Egli Deborah t"), 1)

    def test_different_first_names_with_nickname(self):
        self.assertEqual(self.name_processor.count_unique_names("abigail", "Egni", "abby", "Egni", "al Egni"), 2)

    def test_different_first_names_with_different_names_on_card(self):
        self.assertEqual(self.name_processor.count_unique_names("Alexander ron", "Egni", "al", "Egni", "Deborah Egni"), 2)

    def test_nickname_with_middle_name_in_card(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah", "Egni", "Debbie", "Egni", "Deborah you Egni"), 1)

    def test_nickname_with_different_and_middle_name_in_card(self):
        self.assertEqual(self.name_processor.count_unique_names("Deborah rer", "Egni", "Debbie", "Egni", "Michele ntr Egni"), 2)


if __name__ == '__main__':
    unittest.main()
