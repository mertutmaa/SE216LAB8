class ArchiveItem:
    uid = None
    title = None
    year = None
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        print("ID: ", self.uid, "\nTitle: ", self.title, "\nYear: ",self.year)

    def __eq__(self, uid):
        if self.uid == uid:
            print("uids are equal")
        elif self.uid > uid:
            print("First one is larger" , self.uid)
        else:
            print("Second one is larger: ", uid)

    def is_recent(self, n):
        if n.year >= (2025 - n):
            return True


class Article(ArchiveItem):
    journal = None
    doi = None

    def __init__(self, journal, doi, uid, title, year):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def  __str__(self):
        ArchiveItem.__str__(self)
        print("Journal: ", self.journal, "\nDOI: ", self.doi)


class Podcast(ArchiveItem):
    host = None
    duration = None

    def __init__(self, uid, title, year, host, duration, ):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def  __str__(self):
        ArchiveItem.__str__(self)
        print("Host: ", self.host, "\nDuration: ", self.duration)


class Book(ArchiveItem):
    author = None
    pages = None

    def __init__(self, author, pages, uid, title, year):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        ArchiveItem.__str__(self)
        print("Author: ", self.author, "\nPages: ", self.pages)


def  save_to_file(items, filename):
    f = open(filename, "w+")
    for currentItem in items:
        if(isinstance(currentItem, Book)):
            f.write(f"Book,{currentItem.uid},{currentItem.title},{currentItem.year},{currentItem.author},{currentItem.pages}")
        elif(isinstance(currentItem, Podcast)):
            f.write(f"Podcast,{currentItem.uid},{currentItem.title},{currentItem.year},{currentItem.host},{currentItem.duration}")
        elif(isinstance(currentItem, Article)):
            f.write(f"Article,{currentItem.uid},{currentItem.title},{currentItem.year},{currentItem.doi},{currentItem.journal}")


def load_from_file(filename):
    f = open(filename, 'r')
    for line in f:
        words = line.split(',')
        if(words[0] == 'Book'):
            pass
        elif(words[0] == 'Article'):
            pass
        elif(words[0] == 'Podcast'):
            obj = Podcast(words[1], words[2], words[3], words[4], words[5])
            return obj



def main():
    pass

if __name__ == "__main__":
    main()
