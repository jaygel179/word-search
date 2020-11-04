#!/bin/bash

set -e

echo "Remove caches"
find . | grep -E "(__pycache__|\.pyc|\.pyo$|\.pytest_cache)" | xargs rm -rf

echo "Run WordSearch.py from command line"
python WordSearch.py wordsearch/tests/fixtures/commandline.pzl

echo "Cleaning output files. Making sure we delete all *.out before running the tests"
rm -rf ./tests/fixtures/*.out | true

echo "Runnng pytest"
pytest -v

echo "Done"
