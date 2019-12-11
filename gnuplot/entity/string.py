class String(str):
    def __str__(self):
        return f"\"{super().__str__()}\""

# aliases
Str = String
Path = String
