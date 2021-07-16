#! /bin/bash

echo Installing missing tools

sudo apt-get install -y unzip

echo Installing Chrome

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

echo Installing Chrome Driver

wget https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mkdir /usr/bin/chromedriver
sudo mv ./chromedriver /usr/bin/chromedriver
rm ./chromedriver_linux64.zip