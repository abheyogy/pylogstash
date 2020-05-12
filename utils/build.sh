#!/usr/bin/env bash
# Program to setup the environment for testing this project in the CI/CD.

set -o errexit

sudo apt-get update
sudo apt-get install -y python3-pip python3

# TODO(Pranav): Current working dir logic.
sudo pip3 install -r requirements.txt

echo "Successfully installed dependencies."
