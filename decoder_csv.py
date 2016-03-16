#!/usr/bin/env python3

import os
import sys
import lzma
import glob

def process_file(path):
    basename = os.path.splitext(path)[0]
    decodedname = basename + ".decoded.csv"

    print("process:", path, "->", decodedname)

    with open(path, 'rb') as f:
        data = f.read()

    tempdata = bytearray()

    for i in range(0, 8):
        tempdata.append(data[i])

    for i in range(0, 4):
        tempdata.append(0)

    for i in range(8, len(data)):
        tempdata.append(data[i])

    with open(decodedname, 'wb') as f:
        unpack_data = lzma.decompress(tempdata)
        f.write(unpack_data)

def process_dir(path):
    for filename in glob.iglob(path + '/**/*.csv', recursive=True):
        if "decoded.csv" in filename:
            continue
        process_file(filename)

process_dir(sys.argv[1])
