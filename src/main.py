from name_processor import NameProcessor


def main():

    name_processor = NameProcessor()

    # print("case 1 - extra character to remove, expect 1: ",
    #       name_processor.count_unique_names("Deborah S", "Egli levi", "Deborah", "Egli levi", "Egli levi Deborah"))  # 1
    # print("case 2 - 2 first names, 1 last name, expect 1: ",
    #       name_processor.count_unique_names("Deborah lea", "levi", "Deborah lea", "levi", "levi Deborah lea"))  # 1
    # print("case 3 - spelling check in first name, expect 1: ",
    #       name_processor.count_unique_names("Deboah lea", "levi", "Deborah lea", "levi", "levi Debrah lea"))  # 1
    # print("case 4 - spelling check in middle and first and last names, expect 1: ",
    #       name_processor.count_unique_names("Deborah le", "levi", "Deboah lea", "lei", "levi Deborah lea"))  # 1
    # print("case 5 - different first names, expect 2: ",
    #       name_processor.count_unique_names("Michele", "Egli", "Deborah", "Egli", "Michele Egli"))  # 2
    # print("case 6 - different last names, expect 3: ",
    #       name_processor.count_unique_names("Michele", "Egli", "Deborah", "Houri", "Michele Hamilton"))  # 3
    # print("case 7 - different nicknames to same person, expect 1: ",
    #       name_processor.count_unique_names("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli"))  # 1
    # print("case 8 - same name in different formats, expect 1: ",
    #       name_processor.count_unique_names("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli"))  # 1
    # print("case 9 - different nicknames to same person, expect 1: ",
    #       name_processor.count_unique_names("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli"))  # 1
    # print("case 10 - different spelling in last names, expect 1: ",
    #       name_processor.count_unique_names("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli"))  # 1
    # print("case 11 - last name then first name, expect 1: ",
    #       name_processor.count_unique_names("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah"))  # 1
    # print("case 12 - different first names, expect 2: ",
    #       name_processor.count_unique_names("Michele", "Egli", "Deborah", "Egli", "Michele Egli"))  # 2
    # print("case 13 - different nicknames, expect 2: ",
    #       name_processor.count_unique_names("abigail", "Egni", "abby", "Egni", "al Egni"))  # 2
    # print("case 14 - different first names, expect 2: ",
    #       name_processor.count_unique_names("Alexander ron", "Egni", "al", "Egni", "Deborah Egni"))  # 2
    # print("case 15 - different nicknames with middle name, expect 1: ",
    #       name_processor.count_unique_names("Deborah", "Egni", "Debbie", "Egni", "Deborah you Egni"))  # 1
    # print("case 16 - different names, expect 2: ",
    #       name_processor.count_unique_names("Deborah rer", "Egni", "Debbie", "Egni", "Michele ntr Egni"))  # 2
    #
    # print("case 17 - different family names, expect 3: ",
    #       name_processor.count_unique_names("Deborah", "hamilton", "Deborah", "halton", "Deborah hamiln"))  # 3
    # print("case 18 - simple check by remove space, expect 1: ",
    #       name_processor.count_unique_names("Deborah", " Egli", "Deborah", " Egli", "Deborah Egli"))  # 1
    # print("case 19 - first name with middle name and 2 last names, expect 1:",
    #       name_processor.count_unique_names("Deborah lea", "Egli levi", "Deborah lea", "Egli levi",
    #                                         "Egli levi Deborah lea"))  # 1
    # print("case 20 - 1 first name, 2 last names, and a middle name in card, expect 1:",
    #       name_processor.count_unique_names("Deborah", "Egli levi", "Deborah", "Egli levi",
    #                                         "Egli levi Deborah lea"))  # 1
    # print("case 21 - first name is first in card, expect 1: ",
    #       name_processor.count_unique_names("Deborah", "Egli levi", "Deborah", "Egli levi", "Egli levi Deborah"))  # 1

# The code does not work correctly when we have typo and  nickname
    print("case 22 - first name with typo  and nickname 1: ",
          name_processor.count_unique_names("Deborah", "Egli", "Debbie", "Egli", "Egli  Deorah"))  # 1


    print("case 23 - first name with typo  and nickname 1: ",
          name_processor.count_unique_names("Deborah", "Egli", "Deborah", "Egli", "Egli  Dbbie"))  # 1

    print("case 23 - first name with typo  and nickname: ",
          name_processor.count_unique_names("Debor##ah", "Egli", "Deborah %", "Eg1li", "2Egli  Deb$bie"))# 1


if __name__ == "__main__":
    main()
