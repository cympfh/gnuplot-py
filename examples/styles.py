from gnuplot import Gnuplot, Data
from gnuplot.entity import Path, LineStyle, RGB, Str
import numpy


with Gnuplot() as g:
    g.terminal = 'pngcairo'
    g.output = Path('/tmp/styles.png')

    g.style_line(11, LineStyle(linewidth=2, pointtype=6, linecolor=RGB('#808080')))
    g.border = '3 back ls 11'
    g.tics = 'out nomirror'

    g.style_line(12, LineStyle(linecolor=RGB('#808080'), linetype=0, linewidth=1))
    g.grid = 'back ls 12'

    g.style_line(1, LineStyle(linewidth=2, pointtype=6, linecolor=RGB('#00aaaa'),
                              pointinterval=-1))
    g.pointinterval = 2

    x = numpy.linspace(0, 6.28, 30)
    y = numpy.sin(x) + numpy.random.randn(*x.shape) * 0.1
    data = numpy.stack((x, y)).T
    g.xtics = '0.5 * pi'
    g.format = "x '%.1Ppi"

    g.plot(Data(data, _with='lp', linestyle=1, title=Str('sin + noise')))
