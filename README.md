# Subleq

Little experiments with the single instruction "**SUB**tract and branch if **L**ess-than or **EQ**ual to zero" language based on [this overview](https://esolangs.org/wiki/Subleq).

## Source

No assembler yet, so source is whitespace-delimited three-byte groups in files such as [`helloworld.slq`](helloworld.slq).

Per the above spec example architecture:

- Each instruction is three bytes/operands/addresses: `A B C`

- A `B` operand value of `-1` outputs the ASCII character at address `A` 
- The value in memory address `B` is subtracted from that in address `A`  and placed at address  `B`
- If the value at address `B` is `<=0` , jump to address `C`, else proceed to next instruction

- Coding a jump to a negative address will halt the machine

## Compiler

The "compiler" reads `filename.slq` and creates a binary representation `filename.bin` (big-endian, two's complement).

## Running

The "virtual machine" (such as it is; currently less than 50 LOC) reads `filename.bin` and executes starting the program counter at memory address `0`.

## Example

From `hi.slq`:

```
 9  -1  3 ; output 'H' (ASCII 72)
10  -1  6 ; output 'i' (ASCII 105)
 0   0 -1 ; halt
72 105  0
```

`hi.bin`:

```
09 ff 03 0a ff 06 00 00 ff 48 69 00
```

Output:

```
$ ./subleq.py hi.bin 
Hi
<halt>
```