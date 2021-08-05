import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dic = {row.letter: row.code for (index, row) in nato.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    try:
        nato_list = [alphabet_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters.\n")
    else:
        print(nato_list)
        break
