#!/bin/sh

pytest tests.py
mypy route
flake8 route tests.py
