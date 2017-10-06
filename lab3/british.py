# -*- coding: utf-8 -*-

import argparse
import random


def word_shuffle(word, use_random):
    if not word:
        return
    elif word.__len__() <= 2:
        return word

    letters_to_shuffle = list(word[1:-1])
    if use_random:
        random.shuffle(letters_to_shuffle)
    else:
        letters_to_shuffle = sorted(letters_to_shuffle)
    return word[0] + ''.join(letters_to_shuffle) + word[-1]


def shuffle(text, use_random=False):
    text = unicode(text, "utf-8")
    return '\n'.join(' '.join(word_shuffle(word, use_random) for word in text_line.split())
                     for text_line in text.splitlines())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shuffle letters of text')
    parser.add_argument('-s', '--str', type=str, help="the string whose letters will be shuffled")
    parser.add_argument('-p', '--path', help="path to file which text will be shuffled", type=str)
    parser.add_argument('-r', '--random', help="flag which indicate whether random shuffle will be used or not",
                        action="store_true")
    args = parser.parse_args()

    if args.str is None and args.path is None:
        parser.error("at least one of --str or --path required")

    if args.str:
        print shuffle(args.str, args.random)
    else:
        with open(args.path, 'r') as content_file:
            print shuffle(content_file.read(), args.random)
