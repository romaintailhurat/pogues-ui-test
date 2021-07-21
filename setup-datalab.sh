#! /bin/bash

echo Installing missing tools

sudo apt-get install -y unzip
sudo apt-get install zlib1g-dev

echo Installing Chrome

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

echo Installing Chrome Driver

wget https://chromedriver.storage.googleapis.com/92.0.4515.43/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mkdir /usr/bin/chromedriver
sudo mv ./chromedriver /usr/bin/chromedriver
rm ./chromedriver_linux64.zip

echo Installing pyenv

if [ -d "/home/coder/.pyenv" ]; then
  rm -rf "/home/coder/.pyenv"
fi

curl https://pyenv.run | bash
echo "" >> ~/.bashrc

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

echo Installing Poetry

if [ -d "$HOME/.poetry/" ]; then
  rm -rf "$HOME/.poetry/"
fi

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
.  $HOME/.poetry/env

echo "" >> ~/.bashrc
echo "export PATH=\"$HOME/.poetry/bin:/usr/bin/chromedriver:$PATH\"" >> ~/.bashrc

. ~/.bashrc