import re


class PlotOptions:

    def __init__(self, **kwargs):
        self.options = kwargs

    def __str__(self):
        opts = []
        head_underscore = re.compile(r'^_*')
        for name, value in self.options.items():
            name = head_underscore.sub('', name)
            if value is True:  # e.g. `matrix`
                opts.append(name)
            elif isinstance(value, tuple):  # for `using`
                value = ':'.join(str(x) for x in value)
                opts.append(f"{name} {value}")
            else:
                opts.append(f"{name} {str(value)}")

        return ' '.join(opts)

