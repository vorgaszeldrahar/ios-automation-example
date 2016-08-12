#!/usr/bin/env bash
set -e

# Remove the old virtualenv
rm -rf ./env/

# Create a fresh one
virtualenv -p python3.4 env

# activate the virtualenv
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tests
python main.py
