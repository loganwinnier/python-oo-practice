from random import choice as random_choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    """

    # for testing: '/usr/share/dict/words'

    def __init__(self, path):
        """creates word reader from input file and prints # of words read"""
        print('inside parent __init__')
        self.words = self.word_reader(path)
        print(f'{len(self.words)} words read')

    def __repr__(self):
        return f'<WordFinder self.words={self.words}>'

    def word_reader(self, path):
        """reads input file line-by-line and creates list with each line read
        """
        print('inside parent word_reader')
        open_file = open(path, 'r')
        return [word.strip() for word in open_file]

    def random(self):
        """returns random word from input word list
        """
        ran_word = random_choice(self.words)
        print(ran_word)
        return ran_word

class SpecialWordFinder(WordFinder):
    ''''''

    def word_reader(self, path):
        print('inside child word_reader')
        words = super().word_reader(path)
        return [word for word in words if not word.startswith('#') and word != '']


