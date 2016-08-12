#!/usr/bin/env bash
set -e

# Launch Appium using the same command as the App
'/Applications/Appium.app/Contents/Resources/node/bin/node' /Applications/Appium.app/Contents/Resources/node_modules/appium/build/lib/main.js --address "127.0.0.1" --session-override --debug-log-spacing --platform-version "8.1" --platform-name "iOS" --show-ios-log --default-device &

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

# Kill Appium
# kill $(ps -ef | grep "node appium" | head -1 | cut -d " " -f 4)
