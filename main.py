def main():
    path = "./books/frankenstein.txt"
    with open(path) as f:
        # print( f.read() )
        print( count_words(f.read()) )
    

def count_words(string):
    return len(string.split())


main()