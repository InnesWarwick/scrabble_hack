import csv
import argparse

def get_words():
    with open('dictionary.csv') as words:
        return [w.strip('\n') for w in words]

def filter_words(hand: list[str])-> list[str]:
    words = get_words()
    hand_letter_occurences = {ch: hand.count(ch) for ch in hand}
    def check(word: dict[str,int]) -> bool:
        for word_ch, word_ch_count in word.items():
            if word_ch not in hand:
                return False
            if hand_letter_occurences[word_ch] < word_ch_count:
                return False
            if word_ch_count >= 2:
                return False
            
        return True

    word_letter_occurences_list  = [{ch: word.count(ch) for ch in word} for word in words]
    filtered_words = \
        [word for word_ch_occurences, word in zip(word_letter_occurences_list, words) if check(word_ch_occurences)]
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

def find_best_word(words, max_length):
    letter_value = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    high_score = 0
    high_word = []
    for w in filter(lambda x: len(x) <= max_length, words):
        score = sum([letter_value[l] for l in w])
        if score > high_score:
            high_score = score
            high_word = [w]
        elif score == high_score:
            high_word.append(w)
    return high_word

def solve(args):
    letters = [l for l in args.letters]
    output = find_best_word(filter_words(letters), args.length)
    return output

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    gen_parser = subparsers.add_parser("solve")
    gen_parser.add_argument("letters")
    gen_parser.add_argument("--length", type=int, default=255)
    gen_parser.set_defaults(func=solve)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        print(args.func(args))

if __name__ == "__main__":
    main()

