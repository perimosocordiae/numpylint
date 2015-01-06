# numpylint

A linter for numeric Python code.

Install from source with: `python setup.py install`.
This adds the script `numpylinter.py` to your PATH.

Usage:

    $ numpylinter.py -h
    usage: numpylinter.py [-h] [-v] [--overwrite] FILE [FILE ...]

    positional arguments:
      FILE           File(s) to lint

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose
      --overwrite

Simply point it at one or more python files, and let it tell you what it finds.
Use the --verbose flag to output diffs of the proposed changes,
and use the --overwrite flag to actually modify the file(s).
