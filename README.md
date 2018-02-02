# gnuplot-py
A gnuplot binding for Python

## a sample code

```python
from gnuplot import Gnuplot, Figure


with Gnuplot(debug=True) as g:
    g.set('terminal', 'pngcairo')
    g.set('output', '"/tmp/out.png"')

    fig = Figure('"< seq -10 10 | awk \'$0=$0*$0\'"')._with('lines')
    g.plot(fig)
```
