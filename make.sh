#!/bin/bash
source ~/.bash_profile
conda activate
cd build
chmod +x app.py
./app.py
cd ../
