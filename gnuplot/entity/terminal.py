import re


class Terminal:

    def __init__(self, name: str, **kwargs):
        self.name = name
        self.options = kwargs

    def str_options(self) -> str:
        opts = []
        head_underscore = re.compile(r'^_*')
        for name, value in self.options.items():
            name = head_underscore.sub('', name)
            if value is True:
                opts.append(name)  # e.g. `enhanced`, `persist`
            elif isinstance(value, tuple):  # for `size`
                value = ','.join(str(x) for x in value)
                opts.append(f"{name} {value}")
            else:
                opts.append(f"{name} {str(value)}")

        return ' '.join(opts)

    def __str__(self) -> str:
        return f"{self.name} {self.str_options()}"
