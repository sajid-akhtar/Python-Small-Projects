import pandas

csv_data = pandas.read_csv(
    "D:/Python/python/NATO-Phonetic-Pandas/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}

# print(nato_dict)

name = input("Enter your name: ").upper()
nato_list = [nato_dict[s] for s in name]

print(nato_list)
