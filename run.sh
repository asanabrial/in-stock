#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"

# Activate the virtual environment
source $DIR/.venv/bin/activate

# Run the Python script
python $DIR/main.py
