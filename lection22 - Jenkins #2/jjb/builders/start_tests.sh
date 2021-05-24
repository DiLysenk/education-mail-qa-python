#!/usr/bin/env bash
cd code




export PATH="$PATH:/Library/Frameworks/Python.framework/Versions/3.8/bin/"

cmd="pytest -s -l -v tests/test.py -n $TEST_THREADS --alluredir $WORKSPACE/alluredir"

if [ -n "$KEYWORD" ]; then
    cmd="$cmd -k $KEYWORD"
fi

docker ps -a

$cmd || true