#!/bin/bash

cd src
make clean
make -f makefiles/Makefile.gfortran_mpi all lib tools

cd ../python3
python setup.py build_ext --inplace

cd ..
#end
