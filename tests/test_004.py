"""
plotting matrix data
"""
import os

from gnuplot import Figure, Gnuplot


def test_matrix_2d():

    out_path = '/tmp/test_004.2d.png'
    os.path.exists(out_path) and os.unlink(out_path)

    with Gnuplot() as g:
        g.set('terminal', 'png')
        g.set('output', f"\"{out_path}\"")

        data = [
                [i * j for j in range(10)]
                for i in range(10)]
        g.var('$dat', data)

        fig = Figure('$dat', matrix=True)
        g.plot(fig)

    assert os.path.exists(out_path)
    os.path.exists(out_path) and os.unlink(out_path)


def test_matrix_3d():

    out_path = '/tmp/test_004.3d.png'
    os.path.exists(out_path) and os.unlink(out_path)

    with Gnuplot() as g:
        g.set('terminal', 'png')
        g.set('output', f"\"{out_path}\"")

        data = [
                [i * j for j in range(10)]
                for i in range(10)]
        g.var('$dat', data)

        fig = Figure('$dat', matrix=True, _with='lines')
        g.splot(fig)

    assert os.path.exists(out_path)
    os.path.exists(out_path) and os.unlink(out_path)
