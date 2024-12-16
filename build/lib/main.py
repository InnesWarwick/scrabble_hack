import csv
import argparse

def get_words():
    with open('dictionary.csv') as words:
        return [w.strip('\n') for w in words]

def filter_words(letters):
    words = get_words()
    filtered_words = []
    for w in words:
        letters_copy = letters.copy()
        safe = []
        for wl in w:
            if wl in letters_copy:
                letters_copy.remove(wl)
                safe.append(True)
            else:
                safe.append(False)
        if all(safe):
            filtered_words.append(w)
                    
    return filtered_words

def find_best_word(words):
    letter_value = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    high_score = 0
    high_word = []
    for w in words:
        score = 0
        score = sum([letter_value[l] for l in w])
        if score > high_score:
            high_score = score
            high_word = [w]
        elif score == high_score:
            high_word.append(w)
    return high_word

def solve(args):
    letters = [l for l in args.letters]
    output = find_best_word(filter_words(letters))
    return(output)



def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    gen_parser = subparsers.add_parser("solve")
    gen_parser.add_argument("letters")
    args = parser.parse_args()
    print(solve(args))

if __name__ == "__main__":
    main()