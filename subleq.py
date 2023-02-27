#!/usr/bin/env python

from sys import argv, exit

mem=[]

try:
    with open(argv[1], 'rb') as input:
        contents=input.read()
        if len(contents) % 3:
            print(f'Bad file length {len(contents)}')
            exit()
        for byte in contents:
            mem.append(int.from_bytes([byte], byteorder='big', signed=True))
except:
    print(f'Usage: {argv[0]} <program.bin>')
    exit()

pc=0

def halt():
    print('\n<halt>')
    while True:
        pass

try:
    while True:
        (a,b,c) = (mem[pc],mem[pc+1],mem[pc+2])

        if (b == -1):
            print(chr(mem[a]), end='')
        else:
            mem[b] = mem[b] - mem[a]

            if mem[b] <= 0:
                pc=c
                if pc < 0:
                    halt()
                else:
                    continue

        pc=pc+3

except KeyboardInterrupt:
    pass

except:
    print('Program exception!')
    halt()