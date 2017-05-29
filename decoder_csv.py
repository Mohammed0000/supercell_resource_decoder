#!/usr/bin/env python3

import sys
import glob
from lib_csv import decode_file

def decode_dir(path):
    for filename in glob.iglob(path + '/**/*.csv', recursive=True):
        if "decoded.csv" in filename:
            continue
        decode_file(filename)

decode_dir(sys.argv[1])
