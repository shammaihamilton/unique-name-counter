class NameNormalizer:

    def normalize(self, name):
        name = name.lower().strip()
        return self.remove_one_letter_name(name)

    def remove_one_letter_name(self, name):
        names = name.split()
        if len(names) == 1:
            return name
        if len(names[0]) == 1:
            return names[1]
        if len(names[1]) == 1:
            return names[0]
        return name