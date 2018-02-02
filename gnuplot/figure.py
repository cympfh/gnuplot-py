class Figure():

    def __init__(self, dataname, title=None, _with=None):
        self.dataname = dataname
        self.title = title
        self._with = _with

    def __str__(self):
        statement = self.dataname
        if self._with:
            statement += f" with {self._with}"
        if self.title:
            statement += f" title '{self.title}'"
        return statement

    def _with(self, style):
        self._with = style
        return self
