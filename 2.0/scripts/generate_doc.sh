#! /bin/bash

# you need to install sphinx

sphinx-apidoc -o ../docs/ ../src/
cd ../docs/
make html


