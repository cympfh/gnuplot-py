class Figure():

    def __init__(self, dataname, title=None):
        self.dataname = dataname
        self.title = title

    def __str__(self):
        statement = self.dataname
        if self.with_style:
            statement += f" with {self.with_style}"
        if self.title:
            statement += f" title '{self.title}'"
        return statement

    def _with(self, style):
        self.with_style = style
        return self
