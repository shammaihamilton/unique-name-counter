from nicknames import NickNamer

class NicknameHandler:
    def __init__(self):
        self.nn = NickNamer()

    def get_all_related_names(self, name):
        """Get all related names (both nicknames and canonical names) for a given name."""
        related_names = self.nn.nicknames_of(name) | self.nn.canonicals_of(name)
        related_names.add(name.lower().strip())  # Include the original name in lowercase and stripped
        return related_names

    def get_first_names(self, name, name1, name2):
        """Check the length of the names and format them correctly."""
        lst_name = []
        for i in [name, name1, name2]:
            if len(i.split()) == 1:
                lst_name.append(i.lower().strip())
            else:
                lst_name.append(i.split()[0].lower().strip())
        return lst_name

    def count_persons_by_nickname(self, name, name1, name2):
        """Count the number of unique persons represented by three names."""
        fix_name1, fix_name2, fix_name3 = self.get_first_names(name, name1, name2)

        related_names1 = self.get_all_related_names(fix_name1)
        related_names2 = self.get_all_related_names(fix_name2)
        related_names3 = self.get_all_related_names(fix_name3)


        # Create a list of all related name sets
        all_related = [related_names1, related_names2, related_names3]

        # Use a set to track unique groups
        unique_groups = []

        for related_names in all_related:
            added = False
            for group in unique_groups:
                if not group.isdisjoint(related_names):
                    group.update(related_names)
                    added = True
                    break
            if not added:
                unique_groups.append(related_names)

        # The number of unique groups represents the number of unique persons
        return len(unique_groups)

