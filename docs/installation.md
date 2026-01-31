# Installation

## Prerequisites

- Python 3.7 or higher
- A Google Earth Engine account
- **Optional (for advanced plotting):**
  - R installation (v4.0+)
  - R packages: `ggplot2`, `tmap`, `ggspatial`, `sf`, `dplyr`

## Install via pip

You can install `geeassistant` directly from PyPI (once published):

```bash
pip install geeassistant
```

## Install from Source

To install the latest development version from GitHub:

```bash
git clone https://github.com/pulakeshpradhan/geeassistant.git
cd geeassistant
pip install .
```

## Verify Installation

To verify that the package is installed correctly, open a Python shell and run:

```python
import geeassistant
print(geeassistant.__version__)
```
