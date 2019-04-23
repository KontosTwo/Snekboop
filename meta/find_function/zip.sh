#!/usr/bin/env bash

rm function.zip
cd venv
cd lib
cd python3.7
cd site-packages
zip -r9 ../../../../function.zip .
cd ../../../../
zip -g function.zip function.py