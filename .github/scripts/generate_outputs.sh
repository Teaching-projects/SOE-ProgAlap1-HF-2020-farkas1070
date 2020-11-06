#!/bin/bash
rm -f *.out
for case in `ls tests/*.in`; do
    python3 ./solution.py < $case > "$case.out"
done;
