#!/bin/bash

python -m black src
python -m flake8 src/
