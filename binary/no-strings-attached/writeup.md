# Title

## Authors
- @joooooooooooooooooooooooooooooooooooosh

## Category
- Binary Exploit

## Description
This time there's no way you can guess my password, I'm sure of it. I'm so confident you can't guess my password I'll even let you have the source code for my system...

## Difficulty
- Easy

## Points
75

## Files
- vuln: binary to pwn
- vuln.c: source code for the binary

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Whenever you accept user input, if the user gives more input than you expected and you don't check for that/allocate space for it then the user input can overwrite other parts of memory.

### Walkthrough
1. Looking at the source code, we can see that there is a 20 byte buffer to store our input as well as a variable that stores our permissions.
2. Our user input is read by scanf(), but crucially there's no kind of length check or enforcement, so we can give as much data as we want and start writing into other areas of memory. [LiveOverflow has some great videos explaining this in detail](https://www.youtube.com/watch?v=T03idxny9jE).
3. If we give too much input, we'll cause the program to crash before we get to print out the contents of `flag.txt`. Enter any string of 21-24 characters to successfully change the value of `is_admin` without crashing the program!

### Solution
`python2 -c "print 'A' * 21" | ./vuln`
 
### Flag
`NEWBIE{aLway5_ch3ck_y0ur_buff3r_Lengths}`
</details>
