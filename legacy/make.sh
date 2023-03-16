#!/bin/bash
source ~/.bash_profile
conda activate batman
cd build
chmod +x app.py
./app.py
cd ../
