#!/usr/bin/env python3
"""Count words"""

import os
import sys
from functools import reduce

print(reduce(lambda x, _: x + 1, os.stdin, 0))
