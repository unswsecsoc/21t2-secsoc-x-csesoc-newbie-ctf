# Base64 Onion

## Authors
- Nick (@N-Tandiono) 😃

## Category
- Crypto

## Description
I encoded my message in Base64 again, and again, and again, and again... You get the idea...

## Difficulty
- Medium

## Points
80

## Files
- base-onion.txt: a file containing the flag encoded

## Solution

### Idea
- Testing basic programming skills in security
- Playing around with the Base64 library
- Can still be done without programming if they were ambitious

### Walkthrough
- I included the `gen.py` script (base64 encode flag 36 times)
    - Any more than that and your computer could crash when opening the file which isn't very fun... (but entirely possible - just not for a beginner CTF in my opinion)
- `solve.py` is a possible solution
- You could also use an online decoder to do it without coding 😊

### Flag
SHA256 encoded: `8af541c2c46dbb140fb78f963142ba82924ec2f7a5a3a5b8ba26f6917c2d0f97`

Linux Command: `echo -n NEWBIE{WHATEVER_IS_HERE} | sha256sum`

Or use a SHA256 hash encryptor.

</details>