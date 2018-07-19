#!/bin/bash

cd src
make -f makefiles/Makefile.gfortran_serial all lib tools

cd ../python3
python setup.py build_ext --inplace

cd ..
#end
