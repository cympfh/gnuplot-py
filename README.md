# gnuplot-py
A gnuplot binding for Python

## install

```bash
pip install -U git+https://github.com/cympfh/gnuplot-py.git
```

## sample codes

```python
from gnuplot import Gnuplot, Figure


with Gnuplot(debug=True) as g:
    g.set('terminal', 'pngcairo')
    g.set('output', '"/tmp/out.png"')

    fig = Figure('"< seq -10 10 | awk \'$0=$0*$0\'"')._with('lines')
    g.plot(fig)
```

```python
import numpy
from gnuplot import Figure, Gnuplot


with Gnuplot() as g:
    g.set('terminal', 'png')
    g.set('output', '"/tmp/out.png"')
    g.set('grid')

    X = numpy.linspace(-10, 10)
    Y = X ** 3
    dat = numpy.vstack((X, Y)).transpose()
    g.var('$dat', dat)

    fig = Figure('$dat', _with='lines', title='x^3')
    g.plot(fig)
```

See `tests/` for more samples.
