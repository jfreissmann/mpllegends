from mpllegends.entries import Line, Marker, Rectangle
from mpllegends.legend import Legend


def basetest():
    legend = Legend(fontfamily='serif', fontweight='bold', fontsize='large')

    legend.add_entry(Line(label='Test Line', color='r'))
    legend.add_entry(
        Marker(label='Test Marker', marker='o', facecolor='b', edgecolor='g')
        )
    legend.add_entry(Rectangle(label='Test Rect', color='#111111'))

    legend.create()

    legend.show()


if __name__ == '__main__':
    basetest()
