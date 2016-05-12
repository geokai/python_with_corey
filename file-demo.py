#!/usr/local/bin/python3

# File Objects

with open ('test.txt', 'r') as rf:
    with open ('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write (line)

