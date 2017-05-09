class Chapter:
    def __init__(self, no, title, content):
        self.id = -1
        self.novel_id = -1
        self.no = no
        self.title = title
        self.content = content

    def get_insert_params(self):
        return [self.novel_id, self.title, self.no, self.content]


    def print(self):
        print("{0}, {1}, {2}, {3}, {4}".format(self.id, self.novel_id, self.no, self.title, self.content))
        # print("{0}, {1}, {2}, {3}, {4}".format(self.id, self.novel_id, self.no, self.title, "content"))
