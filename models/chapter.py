class Chapter:
    def __init__(self, novel_id, title, page_number, content):
        self.novel_id = novel_id
        self.title = title
        self.page_number = page_number
        self.content = content

    def get_insert_params(self):
        return [self.novel_id, self.title, self.page_number, self.content]
