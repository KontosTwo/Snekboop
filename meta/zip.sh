#!/usr/bin/env bash

cd deploy 
rm deploy.zip 
zip -r deploy.zip *
cd ..
cd find 
rm find.zip 
zip -r find.zip *
cd ..
cd add_function 
rm add_function.zip 
zip -r add_function.zip *
cd ..
cd find_function 
rm find_function.zip 
zip -r find_function.zip *