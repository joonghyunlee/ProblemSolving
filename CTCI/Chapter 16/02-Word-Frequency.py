class Analyzer(object):
    def __init__(self, book):
        self.wmap = dict()
        words = book.split(' ')
        for word in words:
            keyword = word.lower()
            self.wmap[keyword] = self.wmap.get(keyword, 0) + 1
        print self.wmap

    def count(self, word):
        return self.wmap[word.lower()]


if __name__ == '__main__':
    book = ("Our father in heaven "
            "hallowed be your name "
            "Your kingdom come "
            "Your will be done on earch as it is in heaven "
            "Give us today our daily bread "
            "Forgive use our debts "
            "as we also have forgiven our debtors "
            "And lead us not into temptation "
            "but deliver us from the evil one "
            "For yours is the kingdom and the power"
            "and the glory forever Amen")
    az = Analyzer(book)
    print az.count('your')
