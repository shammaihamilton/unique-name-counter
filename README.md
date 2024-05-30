

Overview:

This module provides a method to count unique names by comparing billing and shipping names with the name on the billing card. 
It normalizes the names, checks for uniqueness, and determines if the names likely represent the same person.

Method Description:

count_unique_names


def count_unique_names(self, bill_first_name, bill_last_name, ship_first_name, ship_last_name, bill_name_on_card):
Parameters

bill_first_name (str): The first name used for billing.
bill_last_name (str): The last name used for billing.
ship_first_name (str): The first name used for shipping.
ship_last_name (str): The last name used for shipping.
bill_name_on_card (str): The name on the billing card.

Returns
int: The number of unique names determined by the comparison logic.

Assumptions:

1. Nickname Constraints: Nicknames cannot have typos.
2. Nickname and Formal Name Relationship: There cannot be two different nicknames and a formal name for the same person.
3. Typo Limitations: Typo mistakes are configured to handle one character difference in a word (can be configured in the name_comparator class).

How It Works
1. Normalization: The input names are normalized using a _name_normalizer utility to ensure consistent comparison.
2. Initial Name Collection: The names are added to a set to track uniqueness.
3. Single Person Check: Checks if the set contains only one unique person.
4. Last Name Extraction: Extracts the last name from the billing card name.
5. Reverse Full Name Check: Rechecks names by extracting the first name from the full name on the billing card.
6. First Name Comparison: Compares the differences in first names and counts matching nicknames.
7. Last Name Comparison: Compares the differences in last names.

Step-by-Step Logic
1. Normalize Input Names:

bill_first_name = self._name_normalizer.normalize(bill_first_name)
bill_last_name = self._name_normalizer.normalize(bill_last_name)
ship_first_name = self._name_normalizer.normalize(ship_first_name)
ship_last_name = self._name_normalizer.normalize(ship_last_name)
bill_name_on_card = self._name_normalizer.normalize(bill_name_on_card)

2. Add Names to Set:

self.add_name_to_set(unique_names, bill_first_name, bill_last_name)
self.add_name_to_set(unique_names, ship_first_name, ship_last_name)
self.add_name_to_set(unique_names, bill_name_on_card)

3. Check Single Person:
if self.is_one_person(unique_names):
    return 1

4. Extract Last Name from Card:

last_name_in_card = self.extract_last_name_from_full_name(bill_last_name, ship_last_name, bill_name_on_card)
if last_name_in_card is None:
    return 3

5. Extract First Name and Recheck:

unique_names.clear()
first_name_in_card = self.extract_first_name_from_full_name(last_name_in_card, bill_name_on_card)
self.add_name_to_set(unique_names, bill_first_name, bill_last_name)
self.add_name_to_set(unique_names, ship_first_name, ship_last_name)
self.add_name_to_set(unique_names, first_name_in_card, last_name_in_card)

if self.is_one_person(unique_names):
    return 1


6. Compare First Names:

amount_of_diff_first_name = self._name_comparator.amount_of_diff_names(
    [first_name_in_card, bill_first_name, ship_first_name])
amount_matching_nicknames = self._nickname_handler.count_persons_by_nickname(first_name_in_card,
                                                                             bill_first_name, ship_first_name)

if amount_of_diff_first_name > 1 and amount_matching_nicknames == 3:
    return 3

7. Compare Last Names:

amount_of_diff_last_name = self._name_comparator.amount_of_diff_names(
    [last_name_in_card, bill_last_name, ship_last_name])

if (amount_of_diff_first_name == 0 or amount_matching_nicknames == 1) and amount_of_diff_last_name == 0:
    return 1

8. Return Matching Nicknames:

return amount_matching_nicknames

Dependencies:

_name_normalizer: Utility for normalizing names.
_name_comparator: Utility for comparing name differences.
_nickname_handler: Utility for counting persons by nickname.
add_name_to_set: Adds normalized names to a set.
is_one_person: Checks if the set contains only one unique person.
extract_last_name_from_full_name: Extracts the last name from the full name on the card.
extract_first_name_from_full_name: Extracts the first name from the full name on the card.
