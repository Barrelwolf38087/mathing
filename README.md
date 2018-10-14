# Mathing
A collection of Python 3.x scripts to make tedious math quicker.
Most of them can either be run directly or used as modules.

## Modules

### factor.py

Outputs a newline-sepearted list of factors.
```bash
$ ./factor.py 21
1
3
7
21 
```

### factorpairs.py

Outputs tuple factors of a number

```bash
$ ./factorpairs.py 24
(1, 24)
(2, 12)
(3, 8)
(4, 6)
```

### gcf.py

Finds the GCF of all given integers.

```bash
$ ./gcf.py 12 32
4
```

### perfect.py

Prints 'True' if the N-th root of X is a natural number,
where N is the first argument and X is the second.

```bash
$ ./gcf.py 2 16
True
$ ./gcf.py 2 7
False
```

## Currently broken or incomplete:
unittests.py

## Notes on Unit Tests Operation
Some tests are skipped by default, because some modules aren't fully implemented yet.
You can avoid skipping these tests with something like this:

### *NIX
```bash
env MATHING_NOSKIPTEST="1" unittests.py
```

### Windows (cmd.exe, not PowerShell)
```
set MATHING_NOSKIPTEST="1"
python3 unittests.py
```
