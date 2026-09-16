"""Test-wide matplotlib setup.

Several tests build a figure themselves and assert its exact pixel size, so they need a backend
with a fixed device pixel ratio: a GUI backend saves at 2x on a HiDPI display and those
assertions fail. The library used to set this for them, as a side effect of importing
``xmovie.core``; now that rendering scopes the backend to itself (see ``xmovie.core.headless``),
the tests declare what they need.
"""

import matplotlib

matplotlib.use("Agg")
