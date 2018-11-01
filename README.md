# Mathing
A collection of Python 3.x scripts to make tedious math quicker.
Most of them can either be run directly or used as modules.

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