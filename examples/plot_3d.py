import numpy
from gnuplot import Data, Gnuplot
from gnuplot.entity import Path, String, Terminal

xyz = numpy.random.normal(size=(1000, 3)) * 3.0
xyz[:, 2] = xyz[:, 0] * xyz[:, 1]

with Gnuplot() as g:
    g.terminal = Terminal('qt', persist=True)
    # g.terminal = Terminal('pngcairo')
    # g.output = Path('/tmp/xy.png')
    g.xlabel = String('x')
    g.ylabel = String('y')
    g.splot(Data(xyz, notitle=True))
