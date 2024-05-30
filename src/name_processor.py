
from name_normalizer import NameNormalizer
from name_comparator import NameComparator
from nickname_handler import NicknameHandler


class NameProcessor:

    def __init__(self):

        self._name_normalizer = NameNormalizer()
        self._name_comparator = NameComparator()
        self._nickname_handler = NicknameHandler()
        self._unique_names = set()

    def add_name_to_set(self, unique_names, first_name, last_name=None):
        if last_name is not None:
            # Add full name if both first and last names are provided
            if first_name or last_name:
                unique_names.add(f"{first_name} {last_name}".strip())
        else:
            # Add first name or last name if only one argument is provided
            if first_name:
                unique_names.add(first_name.strip())

    def is_one_person(self, names):
        return len(names) == 1

    def extract_first_name_from_full_name(self, last_name, full_name):
        # Split the full name and the last name into parts
        last_name_parts = last_name.split()
        full_name_parts = full_name.split()

        # Check if the full name ends with the last name
        if full_name_parts[-len(last_name_parts):] == last_name_parts:
            # If it does, remove the last name parts from the end
            first_name_parts = full_name_parts[:-len(last_name_parts)]
        elif full_name_parts[:len(last_name_parts)] == last_name_parts:
            # If the full name starts with the last name, remove it from the start
            first_name_parts = full_name_parts[len(last_name_parts):]
        else:
            # Otherwise, assume last name is in the middle or mixed in
            first_name_parts = [part for part in full_name_parts if part not in last_name_parts]

        # Join the remaining parts to form the first name
        first_name = ' '.join(first_name_parts)

        return first_name

    def extract_last_name_from_full_name(self, bill_last_name, address_last_name, bill_name_on_card):
        name_parts = bill_name_on_card.split()
        # Check pairs and individual parts
        for i in range(len(name_parts) - 1):
            pair = f"{name_parts[i]} {name_parts[i + 1]}"
            if self._name_comparator.are_similar(bill_last_name, pair) or self._name_comparator.are_similar(
                    address_last_name, pair):
                return pair

        # If no pairs matched, check individual parts
        for name in name_parts:
            if self._name_comparator.are_similar(bill_last_name, name) or self._name_comparator.are_similar(
                    address_last_name, name):
                return name
        return None

    def count_unique_names(self, bill_first_name, bill_last_name, ship_first_name, ship_last_name, bill_name_on_card):
        unique_names = set()

        # Step 1: Normalize input names
        bill_first_name = self._name_normalizer.normalize(bill_first_name)
        bill_last_name = self._name_normalizer.normalize(bill_last_name)
        ship_first_name = self._name_normalizer.normalize(ship_first_name)
        ship_last_name = self._name_normalizer.normalize(ship_last_name)
        bill_name_on_card = self._name_normalizer.normalize(bill_name_on_card)

        self.add_name_to_set(unique_names, bill_first_name, bill_last_name)
        self.add_name_to_set(unique_names, ship_first_name, ship_last_name)
        self.add_name_to_set(unique_names, bill_name_on_card)

        # Step 2: Check if there's only one person - happy flow
        if self.is_one_person(unique_names):
            return 1

        # Step 3: Check if there are 3 different last names
        last_name_in_card = self.extract_last_name_from_full_name(bill_last_name, ship_last_name, bill_name_on_card)
        if last_name_in_card is None:
            return 3

        # Step 4: Check reverse full name
        unique_names.clear()
        first_name_in_card = self.extract_first_name_from_full_name(last_name_in_card, bill_name_on_card)

        # reverse order in card. Add names to the set again for checking
        self.add_name_to_set(unique_names, bill_first_name, bill_last_name)
        self.add_name_to_set(unique_names, ship_first_name, ship_last_name)
        self.add_name_to_set(unique_names, first_name_in_card, last_name_in_card)

        if self.is_one_person(unique_names):
            return 1

        # Step 5: Check if first names are the same
        amount_of_diff_first_name = self._name_comparator.amount_of_diff_names(
            [first_name_in_card, bill_first_name, ship_first_name])
        amount_matching_nicknames = self._nickname_handler.count_persons_by_nickname(first_name_in_card,
                                                                                     bill_first_name, ship_first_name)

        # We need two conditions - for typo mistakes in first names
        if amount_of_diff_first_name > 1 and amount_matching_nicknames == 3:
            return 3

        # Step 6: Check if last names are the same
        amount_of_diff_last_name = self._name_comparator.amount_of_diff_names(
            [last_name_in_card, bill_last_name, ship_last_name])

        if (amount_of_diff_first_name == 0 or amount_matching_nicknames == 1) and amount_of_diff_last_name == 0:
            return 1

        return amount_matching_nicknames




