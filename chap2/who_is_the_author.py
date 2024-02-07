import re
from glob import iglob
from itertools import chain

from toolz import frequencies


def filter_a_the(w):
    """filter out "a" and "the" from a list of words

    Args:
        w (string): a word

    Returns:
        bool: True if w is "a" or "the"

    Examples:
    >>> filter_a_the("a")
    True
    >>> filter_a_the("the")
    True
    >>> filter_a_the("cat")
    False
    """

    return w in ["a", "the"]


class PoemCleaner:
    def __init__(self):
        self.r = re.compile(r"[.,;:?!-]")

    def clean_poem(self, fp):
        with open(fp) as f:
            no_punc = self.r.sub("", f.read())
            return no_punc.lower().split()


def word_ratio(d):
    return float(d.get("a", 0)) / float(d.get("the", 1))


def analyze_poems(poems, cleaner):
    return word_ratio(
        frequencies(filter(filter_a_the, chain(*map(cleaner.clean_poem, poems))))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    cleaner = PoemCleaner()

    author_a_poems = iglob("./author_a/*")
    author_b_poems = iglob("./author_b/*")

    author1_ratio = analyze_poems(author_a_poems, cleaner)
    author2_ratio = analyze_poems(author_b_poems, cleaner)

    print("Original Poem", 0.3)
    print(f"Author 1 ratio: {author1_ratio}")
    print(f"Author 2 ratio: {author2_ratio}")
