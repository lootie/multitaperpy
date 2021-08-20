# multitaperpy
Wraps the Multitaper.jl package so as to work in python

# Installation

Please install using 
```
$ pip install -e git+https://github.com/lootie/multitaperpy.git#egg=multitaperpy
```
Using multitaperpy requires that Julia is installed and in the path, along with
[Multitaper.jl](https://github.com/lootie/Multitaper.jl) and
[PyCall.jl](https://github.com/JuliaPy/PyCall.jl). To install Julia, download a
generic binary from the [JuliaLang site](https://julialang.org/) and 
[add it to your path](https://julialang.org/downloads/platform/). To install Julia
packages required for multitaperpy, open up Python interpreter then run:

```
>>> import multitaperpy
>>> multitaperpy.install()
```

and you're good! Note that one might additionally require

```
>>> from julia.api import Julia
>>> jl = Julia(compiled_modules=False)
```

before one accesses basic functionality, i.e.

```
from multitaperpy import multispec 
import numpy as np

multispec.multispec(numpy.random.rand(100))
```

and you may also need PyJulia

```
$ python3 -m pip install --user julia
```
## Paper

If you make use of multitaperpy, and thus Multitaper.jl, please cite the following paper: [![DOI](https://joss.theoj.org/papers/10.21105/joss.02463/status.svg)](https://doi.org/10.21105/joss.02463).

# Acknowledgment

This material is based upon work supported by the U.S. Department of Energy, Office
of Science, Office of Basic Energy Sciences.
