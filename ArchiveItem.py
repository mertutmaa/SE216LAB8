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

    def __init__(self, uid, title, year, journal, doi, ):
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

    def __init__(self, uid, title, year, author, pages):
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
            f.write(f"Book,{currentItem.uid},{currentItem.title},{currentItem.year},{currentItem.author},{currentItem.pages}\n")
        elif(isinstance(currentItem, Podcast)):
            f.write(f"Podcast,{currentItem.uid},{currentItem.title},{currentItem.year},{currentItem.host},{currentItem.duration}\n")
        elif(isinstance(currentItem, Article)):
            f.write(f"Article,{currentItem.uid},{currentItem.title},{currentItem.year},{currentItem.doi},{currentItem.journal}\n")


def load_from_file(filename):
    f = open(filename, 'r')
    for line in f:
        words = line.split(',')
        if(words[0] == 'Book'):
            obj = Podcast(words[1], words[2], words[3], words[4], words[5])
            return obj
        elif(words[0] == 'Article'):
            obj = Article(words[1], words[2], words[3], words[5], words[4])
            return obj
        elif(words[0] == 'Podcast'):
            obj = Podcast(words[1], words[2], words[3], words[4], words[5])
            return obj



def main():

    b1 = Book("aasd", "bookName", "1999", "name", 50)
    b2 = Book("asd", "bookName2", "2300", "name2", 100)
    p1 = Podcast("uidadsads", "nameCast", 1392, "name3", 300)
    p2 = Podcast("uidadsadsdff", "nameCast2", 1392, "name4", 200)
    a1 = Article("uidarticle1", "articleName1", 1782, "name5", "doi1")
    a2 = Article("uidarticle2", "articleName2", 1783, "name6", "doi2")

    list = [b1, b2, p1, p2, a1, a2]
    save_to_file(list, "test.txt")
    x = load_from_file("test.txt")
    


if __name__ == "__main__":
    main()
