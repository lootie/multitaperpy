# multitaperpy
Wraps the Multitaper.jl package so as to work in python

# Installation

Please install using 
```
pip install -e git+https://github.com/lootie/multitaperpy.git#egg=multitaperpy
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

and you're good!
