# gnuplot-py
A gnuplot binding for Python

## install

```bash
pip install -U git+https://github.com/cympfh/gnuplot-py.git
```

## sample codes

```python
# plot "x * x"

from gnuplot import Gnuplot, Figure
from gnuplot.entity import Path, Terminal

with Gnuplot(debug=True) as graph:
    graph.terminal = Terminal('pngcairo')
    graph.output = Path("/tmp/out.png")
    graph.xrange = (-10, 10)

    fig = Figure("x * x")
    graph.plot(fig)
```


```python
# plot the result of the shell command

from gnuplot import Gnuplot, Figure

with Gnuplot(debug=True) as g:
    fig = Figure('< seq -10 10 | awk "$0 = $0 * $0"', _with='lines')
    g.plot(fig)
```

```python
# plot numpy data

import numpy
from gnuplot import Figure, Gnuplot


with Gnuplot() as g:

    X = numpy.linspace(-10, 10)
    Y = X ** 3
    dat = numpy.vstack((X, Y)).transpose()

    data = Data(dat, _with='lines', title='x^3')
    g.plot(data)
```

See `examples/` for more samples.

### Tip: How to use on Google Colab (or Jupyter Notebook)

```python
# install
!pip install -U git+https://github.com/cympfh/gnuplot-py.git
!apt install gnuplot

# plot
with Gnuplot() as g:
    g.output(Path('/tmp/out.png'))
    ...
    g.plot(...)

# display!
from IPython.display import Image
Image('/tmp/out.png')    
```
