def main():
    path = "./books/frankenstein.txt"
    text = get_text(path)
    words = count_words(text)
    characters = count_characters(text)    
    print( characters )
    

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

main()