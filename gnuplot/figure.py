from gnuplot.entity import PlotOptions


class Figure:

    def __init__(self, expression: str, **kwargs):
        self.expression = expression
        self.options = PlotOptions(**kwargs)

    def __str__(self) -> str:
        return f"{self.expression} {self.options}"
