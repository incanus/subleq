#!/usr/bin/env python

from sys import argv, exit

program=bytearray()

try:
    with open(argv[1], 'r') as input:
        contents=input.read()
        lines=contents.split('\n')
        for line in lines:
            for chunk in line.split(' '):
                chunk=chunk.strip(' ')
                if len(chunk):
                    b=(int(chunk)).to_bytes(1, byteorder='big', signed=True)
                    program.extend(b)
        output_file = argv[1].replace('slq', 'bin')
        with open(output_file, 'wb') as output:
            output.write(program)
            print(f'Wrote {len(program)} bytes to {output_file}')
except:
    print(f'Usage: {argv[0]} <program.slq>')
    exit()