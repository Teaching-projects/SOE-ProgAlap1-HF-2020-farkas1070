#!/bin/bash

LOG="log.txt"
TMP="tmp.txt"
DIR=$1

cd $DIR
rm -f $LOG

[[ -d tests ]] &&
for case in `ls tests/*.in`; do
    generated="$case.gen"
    rm -f $generated
    correct="$case.out"
    python3 main.py < $case > $generated

    equals="$(cmp --silent $generated $correct; echo $?)"  
    if [[ $equals -ne 0 ]]; then 
        echo "WRONG output for exercise $DIR, test case: $case" >> $LOG
        echo "--- Input ----------------------------">>$LOG
        cat $case >> $LOG
        echo "--- Correct output -------------------">>$LOG
        cat $correct >> $LOG
        echo "--- Your output ----------------------">>$LOG
        cat $generated >> $LOG
        echo "--- The diff -------------------------">>$LOG
        diff $generated $correct >> $LOG
        echo "--------------------------------------">>$LOG
        echo "">>$LOG
        echo "">>$LOG     
    fi
    rm $generated   
done;

for py in `ls *.py`; do
    if [ "$py" != "main.py" ] && [ "$py" != "generate_input.py" ]; then
        if python3 -m doctest $py > $TMP; then
            echo "Doctest for $py went well"
        else
            cat $TMP >> $LOG
        fi        
    fi
done;

if [[ -f "$LOG" ]] ; then
    echo "Some checks failed:"
    echo
    cat $LOG
    exit 1
else
    echo "All checks passed."
    exit 0
fi
