class Novel:
    def __init__(self, title, author, description, genre):
        self.id = ""
        self.title = title
        self.author = author
        self.description = description
        self.genre = genre

    @classmethod
    def from_row(cls, row):
        novel = Novel(title=row[1], description=row[2], author=row[3], genre=row[4])
        novel.id = row[0]
        return novel

    def get_insert_params(self):
        return [self.title, self.description, self.author, self.genre]

