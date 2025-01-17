def main():
    path = "./books/frankenstein.txt"
    text = get_text(path)
    words = count_words(text)
    characters = count_characters(text)
    print_report(path, words, characters)        

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    alphabet = { }
    lowered = text.lower()
    for char in lowered:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
    return alphabet

def print_report(path, words, characters):
    alphabet = alphabet_only(characters)
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    for char in alphabet:
        print(f"The '{char}' character was found {alphabet[char]}")
    print("--- End report ---")

def alphabet_only(chars):
    only_alphabet = {}
    a = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    for i in a:
        if i[0].isalpha():
                only_alphabet = only_alphabet | { i[0]: i[1] }

    return only_alphabet

main()