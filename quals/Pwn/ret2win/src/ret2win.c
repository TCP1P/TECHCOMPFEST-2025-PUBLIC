#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win() {
    char buf[100];
    FILE *fd = fopen("flag.txt", "r");
    if (fd == 0) {
        printf("flag.txt not found\n");
        exit(-1);
    }
    fgets(buf, sizeof(buf), fd);
    fclose(fd);
    printf("Wow, how did you get here? Here's the flag:\n%s\n", buf);
}

int main() {
    char buf[100];
    printf("Give me your payload: ");
    gets(buf);
}

__attribute__((constructor))
void setup(void) {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
