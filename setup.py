from setuptools import setup

setup(
    name='hiroshiba_python_usercustomize',
    version='1.0',
    py_modules=['usercustomize'],
    description='hiroshiba\'s usercustomize.py',
    install_requires=[
        'Pygments',
        'setproctitle',
    ],
    author='Kazuyuki Hiroshiba',
)
