#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split("[")
    for word in words:
        word_lists = word.split(":")
        if len(word_lists[0])== 11:
            print '%s\t%s' % (word_lists[0], 1)
~                                                                                                                                                            
