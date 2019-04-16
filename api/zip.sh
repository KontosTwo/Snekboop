#!/usr/bin/env bash

cd write 
rm write.zip 
zip -r write.zip *
cd ..
cd query 
rm query.zip 
zip -r query.zip *
cd ..