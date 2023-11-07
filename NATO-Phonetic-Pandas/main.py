import pandas

csv_data = pandas.read_csv(
    "D:/Python/python/NATO-Phonetic-Pandas/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}

# print(nato_dict)


def generate_phonetic():
    name = input("Enter your name: ").upper()
    try:
        nato_list = [nato_dict[s] for s in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
