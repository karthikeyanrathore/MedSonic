#!/bin/bash
source ~/.bash_profile
conda activate batman
cd build
chmod +x api.py
./api.py
cd ../
