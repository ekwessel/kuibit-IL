# Wishlist

Here we collect ideas to improve and extend PostCactus. If you want to
contribute to the project, this a good place where to start. The projects are
sorted in no particular order. The number of [=] along with each idea indicates
the expected difficulty. This parameter increases with the level
of knowledge of PostCactus or of Python required to complete the task.

## Features

* Function to compute spectrogram of TimeSeries. [=]
* Add design noise curves for known detectors. [=]

## Infrastructure

* Improve docstrings.  [==]
  (According to PEP8, the first line should be short and descriptive.)
* Simplify `apply_unary`, `apply_binary`, `apply_to_self` in `series.py`.
  These functions may be turned into decorators, or at least used in a more
  concise way. [==]
* Numba-ify low-level functions. [===]