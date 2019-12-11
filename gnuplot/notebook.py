import gnuplot
from IPython.display import Image, display


class Gnuplot(gnuplot.Gnuplot):

    def __enter__(self):
        super().__enter__()
        self.terminal = 'pngcairo'
        self.output = '"/tmp/tmptmp.png"'
        return self

    def __exit__(self, types, value, tb):
        super().__exit__(types, value, tb)
        display(Image('/tmp/tmptmp.png'))
