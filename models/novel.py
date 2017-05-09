class Novel:
    def __init__(self, title, author, description, image, genre):
        self.id = ""
        self.title = title
        self.author = author
        self.description = description
        self.image = image
        self.genre = genre

    @classmethod
    def from_row(cls, row):
        novel = Novel(title=row[1], description=row[2], author=row[3], image=row[4], genre=row[5])
        novel.id = row[0]
        return novel

    def get_insert_params(self):
        return [self.title, self.description, self.author, self.image, self.genre]

    def print(self):
        print("( {0}, {1}, {2}, {3}, {4}, {5} )".format(self.id, self.title, self.author, self.image, self.description, self.genre))
