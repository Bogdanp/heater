# heater

heater makes heatmaps.  Inspired by heatmappy but more light weight.

## Installation

    pip install heater

## Usage

``` python
from heater import make_heatmap

with open("background.png") as f:
  heatmap = make_heatmap(f, [(1, 2), (3, 4)])
  heatmap.save("output.png")
```

## License

heater is licensed under Apache 2.0.  Please see
[LICENSE] for licensing details.

[LICENSE]: https://github.com/Bogdanp/heater/blob/master/LICENSE
