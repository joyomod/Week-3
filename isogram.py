def is_isogram(string):
    string = string.lower()

    # counting and storing each letter
    letter_count = {}

    # looping through each character in the string
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # checking if any letter occurs more than once
    for item_count in letter_count.values():
        if item_count > 1:
            return False

    return True
