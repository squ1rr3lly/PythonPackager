# Python Packager

## Credits

Github: Squ1rr3lly

Thanks to Ami Mahloof for the Python2 code (https://medium.com/@amimahloof/how-to-package-a-python-project-with-all-of-its-dependencies-for-offline-install-7eb240b27418)

## Usage

### Packing

Copy `setup.py`, `package.py`, `MANIFEST.in`, and optionally this `README.md' to the directory containing the files you want to package.

Modify `MANIFEST.in` to include/exclude the appropriate files and directories.
  - There are comments in that file, or full documentation at https://docs.python.org/3.0/distutils/commandref.html#sdist-cmd

run `python3 setup.py package`
  - This creates a `dist` directory with the genreated tar.gz package file.

### Unpacking

Extract the archive with `tar -xf <filename>`, cd into the directory it creates

*I would highly recommend using a virtual environment. See Caveats below.*

Rebuild the package with `pip3 install -r requirements.txt --no-index --find-links wheelhouse`

## Caveats

### System
The packaging script collects the compiled components from the system it is run on. 
E.g a package created on:
- Windows != MacOS != Debian != Fedora
- Python3.6 != Python3.7

Again, this only applies if you are including *compiled* components in the distribution.

### Virtual Environment
To avoid conflicts, I would always recomend creating and using a venv when unpacking. This will create a Python environment containing only the dependencies for this package, avoiding conflicts.

To do that:
1) `python3 -m venv venv`
2) `source venv/bin/activate`

When you want to leave the virtual environment, simply type:
`deactivate`
