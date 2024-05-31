import re

class NameNormalizer:

    def normalize(self, name):
        name1 = name.lower().strip()
        clean_name = self.remove_non_alphabetical_except_spaces(name1)
        return self.remove_one_letter_name(clean_name)

    def remove_one_letter_name(self, name):
        names = name.split()
        if len(names) == 1:
            return name
        if len(names[0]) == 1:
            return names[1]
        if len(names[1]) == 1:
            return names[0]
        return name

    def remove_non_alphabetical_except_spaces(self, input_string):
        # Use regex to replace all non-alphabetical characters except spaces with an empty string
        cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string)
        return cleaned_string