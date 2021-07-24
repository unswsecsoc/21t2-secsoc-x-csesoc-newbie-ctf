# azerty

## Authors
- Nick (@N-Tandiono) 😃

## Category
- Crypto

## Description
qwerty? Na, azerty! 

`NEZBIE¨&t°z's°h'rd°é°u(e°↵ccent(£`

## Difficulty
- Easy

## Points
75

## Quick Non-Spoiler Notes by Author
- Actually quite a standard type of question which is similar to the replacement CTF challenge which was of lesser points
- History behind this is that the French used this as an adaptation to the more common and standard US qwerty layout (the one you most likely use today) because accents were very hard to do for characters

## Solution
<details>
<summary>Intended Solution</summary>

### Idea
- Just a really basic cipher to show some exposure to more 'different' ciphers
- Also a substitution cipher if you think about it, but you already know what maps with what

### Walkthrough
- Try find azerty keyboard layout and compare with qwerty to decipher.
- Use an online tool/code your own for this keyboard change cipher. 

### Flag
SHA256 encoded: `f056ed2adb5a44c48b4ccbdbbecb66c895a29ca4e2da9e1c67387f7614a69c2c`

Linux Command: `echo -n NEWBIE{WHATEVER_IS_HERE} | sha256sum`
Or use a SHA256 hash encryptor.
