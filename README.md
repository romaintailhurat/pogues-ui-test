# pogues-ui-test

Automated UI tests for Pogues

## Roadmap

- a general direction: using [this](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/) as a reference setup for Python (see the setup script)
- use pyenv for python environment management
- use poetry for deps management
- implement the Page object model in Python: https://www.lambdatest.com/blog/page-object-model-in-selenium-python/
- use splinter over selenium: https://github.com/cobrateam/splinter


## How to use ?

The supported environment for now is inside the SSP Datalab VS code service.

Once the service instantiated, clone the repo then use the setup script to install various dependencies:

```
bash setup-datalab.sh
```

:grimacing: Manually play `. ~/.bashrc` (???)

To install the required Python deps:

```
poetry install
```

At the moment, poetry create its own virtualenv ; in the future we would have pyenv to manage that...

To check everything works, once again in a terminal :

```
# in pogues-ui-test dir
poetry run pytest
```