"""
Plot numpy data
"""

import numpy.random
from gnuplot import Data, Gnuplot
from gnuplot.entity import Path, Terminal

x = numpy.random.normal(size=(1000, 2))
with Gnuplot() as g:
    g.terminal = Terminal('pngcairo')
    g.output = Path('/tmp/rand.png')
    g.plot(Data(x))
