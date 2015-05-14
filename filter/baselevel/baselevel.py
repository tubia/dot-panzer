#!/usr/bin/env python3

"""
reset the base header level for the document

- new base level is set by value passed as argv[2]
- new base level values may be from 1 to 5
"""

import sys
import os
sys.path.append(os.path.join(os.environ['PANZER_SHARED'], 'python'))
import panzertools
from pandocfilters import toJSONFilter, Header

new_level = 1

def rehead(key, value, format, meta):
    if key == 'Header':
        return Header(new_level + (value[0] - 1), value[1], value[2])

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        new_level = max(min(5, int(sys.argv[2])), 1)
    panzertools.log('INFO', 'base header level set to %d' % new_level)
    toJSONFilter(rehead)
