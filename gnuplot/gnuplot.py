import subprocess
import sys
from typing import Any, List, Union

from gnuplot.data import Data
from gnuplot.figure import Figure
from gnuplot.entity import LineStyle


class Gnuplot:

    _attr_hook = False
    _var_id = 0

    def __init__(self, debug=False):
        self.gnuplot = subprocess.Popen(["gnuplot"], stdin=subprocess.PIPE)
        self.debug = debug

    def setattr(self, name: str, value: Any):
        """Primitive __setattr__"""
        super().__setattr__(name, value)

    def __enter__(self):
        """Hack __setattr___"""
        self.setattr('_attr_hook', True)
        return self

    def __exit__(self, types, value, tb):
        """Unhack __setattr___"""
        self.setattr('_attr_hook', False)
        self.gnuplot.__exit__(types, value, tb)

    def write(self, statement: str):
        """Insert command into gnuplot process"""
        self.gnuplot.stdin.write(bytes(statement + '\n', 'utf-8'))
        if self.debug:
            sys.stderr.write(statement + '\n')

    def __setattr__(self, name: str, value: Any):
        """Generic set

        set {name} {value}
        """
        if not self._attr_hook:
            return self.setattr(name, value)

        if isinstance(value, tuple):  # for xrange, yrange
            value = ':'.join('' if x is None else str(x) for x in value)
            self.write(f"set {name} [{value}]")
        elif value is True:
            self.write(f"set {name}")
        else:
            self.write(f"set {name} {str(value)}")

    def style_line(self, index: int, style: LineStyle):
        """Line style"""
        self.write(f"set style line {index} {style}")

    def define_data(self, plots: List[Union[Figure, Data]]):
        for p in plots:
            if isinstance(p, Data):
                varname = f"$var_{self._var_id}"
                self.setattr('_var_id', self._var_id + 1)
                p.varname = varname
                p.define(varname, self.write)

    def plot(self, *ps: Union[Figure, Data]):
        self.define_data(ps)
        self.write("plot " + ','.join(str(p) for p in ps))

    def splot(self, *ps: Union[Figure, Data]):
        self.define_data(ps)
        self.write("splot " + ','.join(str(p) for p in ps))
