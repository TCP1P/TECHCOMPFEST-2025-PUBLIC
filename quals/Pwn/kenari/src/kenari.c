#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

#define BUFFER_SIZE 64

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void hitme() {
    FILE *fp;
    char flag[64];
    fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("File flag.txt tidak ditemukan\n");
        exit(1);
    }

    fgets(flag, sizeof(flag), fp);
    printf("Flag: %s\n", flag);

    fclose(fp);
    
    exit(0);
}

void vuln() {
    char buffer[BUFFER_SIZE];

    printf("username: ");
    gets(buffer);
    printf(buffer);
    printf("\n");
    printf("password: ");
    gets(buffer);

}

int main() {
    init();
    vuln();
    return 0;
}