#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define X 0x100
#define L 0x80
#define M 0x60
#define S 0x40

char *note;

int main(){
    int size, choice;
    for(;;){
        printf(": %s\n> +\n> -\n> ", note ? note : "?");
	if (scanf("%d%*c", &choice) != 1) exit(1);
        switch (choice) {
            case 1:
                if (note) {puts("!!!"); break;}
                printf("$ ");
		if (scanf("%d%*c", &size) != 1) exit(1);
		switch (size){
			case 1: note = (char *)malloc(S); break;
			case 2: note = (char *)malloc(M); break;
			case 3: note = (char *)malloc(L); break;
			case 4: note = (char *)malloc(X); break;
			default: puts("???"); break;
		}
                printf("# ");
                read(STDIN_FILENO, note, X);
		note[strcspn(note, "\n")] = 0;
                break;
            case 2:
		if (!note) {puts("***"); break;}
                free(note);
                note = NULL;
                break;
            default:
                puts("...");
                return 0;
        }
    }
}

__attribute__((constructor))
void init(){
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
