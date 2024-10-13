def number_of_vowels(text):
    count = 0

    for letter in text:
        count += int(letter.lower() in "aoeui")

    return count

print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)