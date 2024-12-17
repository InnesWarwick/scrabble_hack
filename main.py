import csv
import argparse

def get_words():
    with open('dictionary.csv') as words:
        return [w.strip('\n') for w in words]

def filter_words(hand: list[str]) -> list[str]:
    """
    Function to find the list of potential words from the input 
    hand, represented by a list of strings for each character.

    Arguments:
        hand: a list of strings representing the tiles the user has

    Returns:
        A list of words
    """

    words = get_words()

    # Convert the input hand into a dictionary of characters 
    # to integers, representing the count within the hand
    hand_letter_occurences = {ch: hand.count(ch) for ch in hand}

    # Defining a function to check if a word, represented by a dictionary of letter occurences
    # is a valid word that can be played
    def is_valid(word: dict[str,int]) -> bool:
        for word_ch, word_ch_count in word.items():
            if word_ch not in hand:
                return False
            if hand_letter_occurences[word_ch] < word_ch_count:
                return False
            if word_ch_count >= 2:
                return False
            
        return True

    # Transform the list of words into a list of dictionaries of letter occurences for each word
    word_letter_occurences_list  = [{ch: word.count(ch) for ch in word} for word in words]

    # Find the valid words by zipping the words represented by string and the words represented by dicts
    # If the dictionary is found to be valid we add the string to the list
    filtered_words = \
        [word for word_ch_occurences, word in zip(word_letter_occurences_list, words) if is_valid(word_ch_occurences)]
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
    print(args.func(args))

if __name__ == "__main__":
    main()
