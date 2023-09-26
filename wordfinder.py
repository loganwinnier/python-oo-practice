from random import choice as random_choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> new_word = WordFinder('/usr/share/dict/words')

    >>> new_word.word_reader('/usr/share/dict/words')
    True
    """

    def __init__(self, path):
        self.words = self.word_reader(path)

    def word_reader(self, path):
        words = []
        open_file = open(path, 'r')
        for line in open_file:
            words.append(line[:-2])
        open_file.close()
        print(f'{len(words)} words read')
        return words

    def random(self):
        ran_word = random_choice(self.words)
        print(ran_word)
        return ran_word
