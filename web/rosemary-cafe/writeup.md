# arnold's biscuits

## Authors
- @abiramen

## Category
- Web

## Description
Hi! I'm Arnold, founder of Arnold's Biscuits. At Arnold's, we aspire to manufacture high quality gift boxes for your loved ones so that you can give them biscuits to remember you by.

Recently, I hired some cheap freelance web developer online to design a website for me to communicate with my employees with. He made two accounts: one with username `employee` and password `biscuit123`, and another account for me to create the messages, with username `admin`. However, I don't really trust this freelancer's skills since they were so cheap. Could you test the website to make sure no one can get into my account? 

## Difficulty
- Medium

## Points
70

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Demonstrates why using unsigned cookies to authenticate is a bad idea.

### Walkthrough
1. Identify that there seems to be some kind of biscuit theme here. A web developer term that's related to biscuits are cookies!
2. Log in with the provided 'employee' account.
3. Identify that a cookie has been set called 'username', with the value 'employee'. (This was truly a biscuit to remember you by :P)
4. Change the value of the cookie to 'admin'.
5. Refresh the page. The flag should now reveal itself.

You might be asking how a webpage can remember who you are with cookies, when you could change the cookie to say whatever you want instead! This is what a signed token, such as JSON Web Token, is used for. The JWT also contains your username, just like the cookie you found in this challenge, but it also contains a 'signature', which it can use to mathematically verify that the cookie hasn't been tampered with.

### Flag
`NEWBIE{b1scUit5_moR3_L1k3_C00KIE!!_0MN0MN0M}`
</details>
