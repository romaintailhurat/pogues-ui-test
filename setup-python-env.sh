# We take for granted the installation of pyenv
# We need to provide here the uncommon installation path of openssl
# https://github.com/pyenv/pyenv/wiki/Common-build-problems#error-the-python-ssl-extension-was-not-compiled-missing-the-openssl-lib
#
# --------------------
# WARNING still problematic
# --------------------
export CONFIGURE_OPTS="--with-openssl=$(which openssl)"
pyenv install -v 3.9.6
pyenv local 3.9.6