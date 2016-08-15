#!/usr/bin/env bash
set -e

# Appium should already be running, otherwise this will fail

# Remove the old virtualenv
rm -rf ./env/

# Create a fresh one
virtualenv -p python2.7 env

# activate the virtualenv
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tests
python main.py

