"""
plotting 2d-numpy data, 2 columns
"""
import os

import numpy
from gnuplot import Figure, Gnuplot


def plot(**kwds):

    out_path = '/tmp/test_002.png'
    os.path.exists(out_path) and os.unlink(out_path)

    with Gnuplot() as g:
        g.set('terminal', 'png')
        g.set('output', f"\"{out_path}\"")
        data = numpy.random.normal(size=(100, 2))
        g.var('$dat', data)
        fig = Figure('$dat', **kwds)
        g.plot(fig)

    assert os.path.exists(out_path)
    os.path.exists(out_path) and os.unlink(out_path)


def test_title_lines():
    plot(title='title', _with='lines')


def test_title_boxes():
    plot(title='title', _with='boxes')


def test_lines():
    plot(_with='lines')


def test_boxes():
    plot(_with='boxes')


def test_plain():
    plot()
