from typing import NamedTuple, Optional, Union

from gnuplot.entity.color import RGB


class Style:
    pass


class LineStyle(Style, NamedTuple):
    default: bool = False
    linetype: Optional[Union[int, RGB]] = None
    linecolor: Optional[RGB] = None
    linewidth: Optional[float] = None
    pointtype: Optional[int] = None
    pointsize: Optional[float] = None
    pointinterval: Optional[int] = None
    pointnumber: Optional[int] = None
    dashtype: Optional[int] = None

    def __str__(self) -> str:
        if self.default:
            return 'default'
        fields = [
            'linetype',
            'linecolor',
            'linewidth',
            'pointtype',
            'pointsize',
            'pointinterval',
            'pointnumber',
            'dashtype',
        ]
        opts = []
        for f in fields:
            val = getattr(self, f)
            if val is not None:
                opts.append(f"{f} {val}")
        return ' '.join(opts)
