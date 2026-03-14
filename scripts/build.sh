#!/bin/bash
set -e

echo "installing python dependencies..."
pip install -r requirements.txt

echo "cloning tts client..."
git clone https://github.com/nvidia-riva/python-clients.git

echo "setting script permissions..."
chmod +x scripts/tts.sh

echo "dependency instalation complete."
