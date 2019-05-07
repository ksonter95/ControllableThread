@ECHO OFF

:: Delete the previous distribution
del dist

:: Compile the distribution wheel and tar
python setup.py sdist bdist_wheel

:: Upload to PyPi
python -m twine upload dist/*