from typing import Callable

from gnuplot.entity import PlotOptions


class Data:

    def __init__(self, data, **kwargs):
        self.data = data
        self.options = PlotOptions(**kwargs)
        self.varname = None

    def __str__(self) -> str:
        assert self.varname is not None
        assert self.varname.startswith('$')
        return f"{self.varname} {self.options}"

    def define(self, varname: str, write: Callable):
        write(f"{varname} << EOD")
        if self.data.ndim == 1:
            for x in self.data:
                write(str(x))
        elif self.data.ndim == 2:
            for xs in self.data:
                write(' '.join(str(x) for x in xs))
        write('EOD')
