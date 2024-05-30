from Levenshtein import distance as levenshtein_distance

class NameComparator:

    def are_similar(self, name1, name2):
        if abs(len(name1) - len(name2)) <= 1:
            return levenshtein_distance(name1, name2) <= 1
        return False

    def check_exist_middle_in_all_name(self, name, name1, name2):
        name_parts = name.split()
        name1_parts = name1.split()
        name2_parts = name2.split()

        if len(name_parts) == 2 and len(name1_parts) == 2 and len(name2_parts) == 2:
            # if count 2 - no nickname can be
            return True

    def amount_of_diff_names(self, input_names):
        name1_parts = input_names[0].split()
        name2_parts = input_names[1].split()
        name3_parts = input_names[2].split()
        dissimilar_set = set()

        # Compare the first and middle names of each pair
        if len(name1_parts) == 1 or len(name2_parts) == 1:
            if not self.are_similar(name1_parts[0], name2_parts[0]):
                dissimilar_set.add(input_names[0])
                dissimilar_set.add(input_names[1])
        elif len(name1_parts) > 1 and len(name2_parts) > 1:
            if not self.are_similar(name1_parts[0], name2_parts[0]) or not self.are_similar(name1_parts[1],
                                                                                            name2_parts[1]):
                dissimilar_set.add(input_names[0])
                dissimilar_set.add(input_names[1])

        if len(name1_parts) == 1 or len(name3_parts) == 1:
            if not self.are_similar(name1_parts[0], name3_parts[0]):
                dissimilar_set.add(input_names[0])
                dissimilar_set.add(input_names[2])
        elif len(name1_parts) > 1 and len(name3_parts) > 1:
            if not self.are_similar(name1_parts[0], name3_parts[0]) or not self.are_similar(name1_parts[1],
                                                                                            name3_parts[1]):
                dissimilar_set.add(input_names[0])
                dissimilar_set.add(input_names[2])

        if len(name2_parts) == 1 or len(name3_parts) == 1:
            if not self.are_similar(name2_parts[0], name3_parts[0]):
                dissimilar_set.add(input_names[1])
                dissimilar_set.add(input_names[2])
        elif len(name2_parts) > 1 and len(name3_parts) > 1:
            if not self.are_similar(name2_parts[0], name3_parts[0]) or not self.are_similar(name2_parts[1],
                                                                                            name3_parts[1]):
                dissimilar_set.add(input_names[1])
                dissimilar_set.add(input_names[2])

        return len(dissimilar_set)

