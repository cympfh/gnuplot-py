"""
plotting 2d-numpy data, 3 or more columns
"""
import os

import numpy
from gnuplot import Figure, Gnuplot


def test_plot():

    out_path = '/tmp/test_003.png'
    os.path.exists(out_path) and os.unlink(out_path)

    with Gnuplot() as g:
        g.set('terminal', 'png')
        g.set('output', f"\"{out_path}\"")
        data = numpy.random.normal(size=(100, 4))
        g.var('$dat', data)
        fig1 = Figure('$dat', using=[1, 2], title='a')
        fig2 = Figure('$dat', using=[3, 4], _with='lines')
        g.plot(fig1, fig2)

    assert os.path.exists(out_path)
    os.path.exists(out_path) and os.unlink(out_path)
