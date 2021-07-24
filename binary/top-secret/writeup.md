# Title

## Authors
- @joooooooooooooooooooooooooooooooooooosh

## Category
- Binary Exploit

## Description
It's named Top Secret so it must be secure right? Hope nobody finds my password...

## Difficulty
- Easy

## Points
50

## Files
- vuln: binary to pwn

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Strings in C are arrays of characters in memory, there are several ways to uncover those strings.

### Walkthrough
1. Easiest (imo) option is using a command line program called `strings` which goes through the program and prints out any continuous sequences of printable characters it can find.

There's quite a bit of output, but if you scroll through it you can quickly find the strings that are printed out when you run the program normally.

```
[]A\A]A^A_
flag.txt
create a file called 'flag.txt' first
Welcome to My Secure System v1.0
Enter password:
shh_s3cr3t
Sorry, you aren't authorised to do top secret admin stuff.
;*3$"
GCC: (GNU) 11.1.0
```

We can see the beginning text where it asks us for a password, then something that was definitely not printed out by the program, and then the ending text that tells us we don't have permission.

...that `shh_s3cr3t` thing sure looks like a password to me...

Enter that string while running the program and it will successfully print out the contents of whatever `flag.txt` file you have in the current directory.

2. Another way to find the strings is to open the binary in a text editor like Notepad or Vim. Most of the data in the program isn't valid text, but if you scroll through the program the valid strings will stick out and you can get the `shh_s3cr3t` string that way.

### Flag
`NEWBIE{m0r3_Lik3_b0tt0m_s3cr3t}`
</details>
