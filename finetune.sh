#!/bin/bash
# https://beta.openai.com/docs/guides/fine-tuning/cli-data-preparation-tool

set -e

rm -fv examples_prepared*.jsonl

python3 examples.py
openai tools fine_tunes.prepare_data -f examples.csv
openai api fine_tunes.create -t "examples_prepared.jsonl" -m "davinci"
