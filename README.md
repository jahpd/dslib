# Design Sound Library for PureData

This is my personal library of abstractions for [PureData](http://puredata.info/), following some ideas and exercises from Andy Farnnel's[Design Sound](http://mitpress.mit.edu/books/designing-sound) of .

# What do?

Until now, I built some basic abstractions for design spectra
([AM](https://en.wikipedia.org/wiki/Amplitude_modulation),
[FM](https://en.wikipedia.org/wiki/Frequency_modulation)) with some
customized functions, like non-linear ones (that add some nice complex
features to spectra).

Added to some examples and design sound exercises from Andy Farnell [Book](mitpress.mit.edu/books/designing-sound)
granular synthesis:

## Installation

If you have linux or mac, i suggest the following:

    $ git clone https://www.github.com/jahpd/dslib.git

If you have windows, i suggest download github application and then
download the source code from the application.

Open PureData, go to _Prefereces_ and then add the properly path
search;

![http://booki.flossmanuals.net/pure-data/_full/static/PureData-InstallingOSX-osx-install-7-en.png]

In my machine is something like:

    ~/path/to/dslib/

## Additive

Need more time to build some nice thing

## Non-linear

These are simple oscilators transformed by non-linear functions that generated some interesting spectra:

- Chebychev polinomials from 3..9 orders
- Hiperbolic Tangent

## AM

- Common AM (Two side bands minus carrier frequency)
- Ring modulation (Two side bands  + carrier)
- One side band
- Am modulation with non-linear oscilators:
  - Chebychev polinomials from 3..9 orders
  - Hiperbolic tangent

## FM

- Common FM 
- FM modulation with non-linear oscilators:
  - Chebychev polinomials from 3..9 orders
  - Hiperbolic tangent

## Granular

Contains a simple granular oscilator; it read the DSP flow, make an gaussian envelope, and plays repeatdly. It's a simple sampler.

# Future Aims

Make some useful tools to Sound Design works, like videogames or installations; will folow some ideas from Andy Farnell's book and my own ideas.



