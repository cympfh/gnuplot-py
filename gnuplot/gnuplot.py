import sys
import subprocess
import numpy
from gnuplot import figure


class Gnuplot():

    def __init__(self, debug=False):
        self.gnuplot = subprocess.Popen(["gnuplot"], stdin=subprocess.PIPE)
        self.debug = debug

    def __enter__(self):
        return self

    def __exit__(self, types, value, tb):
        self.gnuplot.__exit__(types, value, tb)

    def write(self, statement: str):
        self.gnuplot.stdin.write(bytes(statement + '\n', 'utf-8'))
        if self.debug:
            sys.stderr.write(statement + '\n')

    def set(self, *args):
        self.write("set " + ' '.join(args))

    def var(self, varname: str, data: numpy.array):
        if type(data) != numpy.ndarray:
            data = numpy.array(data)
        self.write(f"{varname} << EOD")

        if data.ndim == 1:
            for x in data:
                self.write(str(x))

        elif data.ndim == 2:
            for xs in data:
                self.write(' '.join(str(x) for x in xs))

        else:
            raise NotImplementedError

        self.write("EOD")

    def plot(self, *ps: figure.Figure):
        self.write("plot " + ','.join(str(p) for p in ps))

    def splot(self, *ps: figure.Figure):
        self.write("splot " + ','.join(str(p) for p in ps))
