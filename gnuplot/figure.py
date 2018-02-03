class Figure():

    def __init__(self, dataname, title=None, _with=None, using=None):
        self.dataname = dataname
        self.title = title
        self._with = _with
        self.using = using

    def __str__(self):

        statement = self.dataname

        if self.using:
            if type(self.using) == str:
                statement += f" u {self.using}"
            elif type(self.using) == list:
                statement += f" u {':'.join(map(str, self.using))}"
            else:
                raise NotImplementedError

        if self._with:
            statement += f" with {self._with}"
        if self.title:
            statement += f" title '{self.title}'"
        return statement
