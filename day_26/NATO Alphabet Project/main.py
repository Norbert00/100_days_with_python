import pandas

file = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in file.iterrows()}

user_word = input("Please type the word: ").upper()

phonetic_code = [nato_alphabet[letter] for letter in user_word]
print(phonetic_code)

