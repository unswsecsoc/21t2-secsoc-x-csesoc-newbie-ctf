#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

int main(int argc, char *argv[])
{
    char buf[20];
    printf("Welcome to My Secure System v1.0\n");
    printf("Enter password: ");
    fflush(stdout);
    scanf("%s", buf);
    if (!strcmp(buf, "shh_s3cr3t")) {
        top_secret_admin_stuff();
    } else {
        printf("Sorry, you aren't authorised to do top secret admin stuff.\n");
    }
    return 0;
}
