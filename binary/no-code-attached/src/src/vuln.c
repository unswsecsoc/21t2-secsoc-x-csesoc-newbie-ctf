#include <stdio.h>
#include <stdlib.h>
// gcc vuln.c -fno-stack-protector -m32

void top_secret_admin_stuff() {
    char buf[50];
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL) {
        printf("create a file called 'flag.txt' first\n");
        exit(1);
    }
    fgets(buf, sizeof(buf), f);
    printf("%s", buf);
}

int vuln() {
    int is_admin = 0;
    int in = 0;
    int p = 0;
    char buf[40];
    printf("Welcome to My Secure System v3.0\n");
    printf("Enter password: ");
    fflush(stdout);
    while ((in = getchar()) != '\n') {
        if (in != 'A' && in != 'a')
            buf[p++] = in;
    }
    return is_admin;
}

int main(int argc, char *argv[])
{
    if (vuln() == 0x4269) {
        top_secret_admin_stuff();
    } else {
        printf("Sorry, you aren't authorised to do top secret admin stuff.\n");
    }
    return 0;
}
