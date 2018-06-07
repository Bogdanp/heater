import os

import numpy
from PIL import Image

from heater import make_heatmap


def path_to(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


def test_can_make_heatmaps():
    points = [(x, y) for x in range(255) for y in range(255)] + \
        [(x, y) for x in range(400, 655) for y in range(400, 655)]

    with open(path_to("fixtures", "bg.png"), mode="rb") as f:
        heatmap = make_heatmap(f, points)

    expected = Image.open(path_to("fixtures", "output.png"))
    assert numpy.array_equal(numpy.array(heatmap), numpy.array(expected))
