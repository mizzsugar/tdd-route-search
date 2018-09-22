#!/bin/sh

pytest tests.py
mypy route.py
flake8 route.py tests.py
