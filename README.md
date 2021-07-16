# pogues-ui-test

Automated UI tests for Pogues

## Roadmap

- use poetry for deps management
- implement the Page object model in Python: https://www.lambdatest.com/blog/page-object-model-in-selenium-python/
- use splinter over selenium: https://github.com/cobrateam/splinter


## How to use ?

The supported environment for now is inside the SSP Datalab VS code service.

Once the service instantiated, use the setup script to install various dependencies:

```
bash setup-datalab.sh
```

Warning: the python dependencies are not yet managed (in the future it will be done by Poetry).

So, manually, in a terminal:

```
pip install pytest selenium
```

To check everything works, once again in a terminal :

```
pytest test/
```