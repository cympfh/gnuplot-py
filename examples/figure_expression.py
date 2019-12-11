"""
Figure given by string expression
"""

from gnuplot import Figure, Gnuplot
from gnuplot.entity import Path, String, Terminal

with Gnuplot() as g:
    g.terminal = 'pngcairo'  # NOTE: str is also ok, but Terminal is recommended
    g.output = Path('/tmp/x2.png')
    g.plot(Figure('x * x'))


with Gnuplot() as g:
    g.terminal = Terminal('pngcairo', size=(700, 400), font=String('Verdana,14'))
    g.output = Path('/tmp/x3.png')
    g.xrange = (-5, 5)
    g.grid = True
    g.plot(Figure('x * x * x'))

with Gnuplot() as g:
    g.terminal = Terminal('pngcairo', size=(700, 400), font=String('Verdana,14'))
    g.output = Path('/tmp/wave.png')
    g.plot(Figure('sin(x)', title=String('sin')),
           Figure('cos(x)', title=String('cos')))
