# Title

## Authors
- @joooooooooooooooooooooooooooooooooooosh

## Category
- Binary Exploit

## Description
Now I'm starting to feel paranoid so I won't give you the source code this time. You'll have to figure it out on your own... Good Luck!

## Difficulty
- Medium

## Points
125

## Files
- vuln: binary to pwn

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Pretty similar to `no strings attached` but you don't have the source code to figure out what's changed...

### Walkthrough
1. You can either read the raw assembly of the program using something like `objdump`, or you can use a decompiler to read the C code using something like `Ghidra` or `Binary Ninja`.
2. We can see a slight change to the `vuln` function: instead of using scanf() to read user input, it gets once character at a time with fgetc() and ignores any A's or a's that it sees. This means if we want to overflow the buffer, we need to use another character (anything else will work).
3. The other crucial change is in main() - instead of checking if the return value of vuln() is not 0, it specifically checks if the return value of vuln() is equal to 0x4269. 0x42 is 'B' in ASCII and 0x69 is 'i' in ASCII, however due to something called 'little-endian' we need to supply our input sort of backwards - i.e. we should overwrite `is_admin` with iB instead of Bi.
4. The last crucial change to the code is the variables used in vuln(). There is now a40 byte buffer to store user input instead of a 20 byte buffer, and a new int variable used for the new user input logic lies in between the buffer and `is_admin`, meaning we need to provide 44 bytes of input before we start overwriting `is_admin`.

### Solution
`python2 -c "print 'B' * 44 + 'iB'" | vuln`

### Flag
`NEWBIE{h4v1ng_th3_c0de_sur3_h3lp5}`
</details>
